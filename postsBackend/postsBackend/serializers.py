from django.contrib.auth.models import User
from rest_framework import serializers
from postsAPI.models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    tags = serializers.ListField(child=serializers.CharField(), required=False)
    
    class Meta:
        model = Post
        fields = ['id','comment', 'username', 'tags']
    
    def validate_tags(self, value):
        valid_users = []
        for tag in value:
            if not tag.startswith("@"):
                raise serializers.ValidationError(f"Invalid tag format: {tag}. Use @username format.")
            username = tag[1:]
            try:
                user = User.objects.get(username=username)
                valid_users.append(user)
            except User.DoesNotExist:
                raise serializers.ValidationError(f"User with username '{username}' does not exist.")
        return valid_users

    def create(self, validated_data):
        tags = validated_data.pop('tags',[])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)
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
        