from django.contrib.auth.models import User
from rest_framework import serializers
from postsAPI.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'username']

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    tags = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', many=True, required=False)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','post', 'caption','username', 'tags', 'comments']

    def validate_tags(self, value):
        valid_users = []
        for tag in value:
            if not isinstance(tag, User):
                raise serializers.ValidationError(f"Invalid tag format: {tag}. Tags must be valid User instances.")
            valid_users.append(tag)
        return valid_users 

    def create(self, validated_data):
        tags = validated_data.pop('tags',[])
        post = Post.objects.create(**validated_data)

        for tag in tags:
            post.tags.add(tag)
        return post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        