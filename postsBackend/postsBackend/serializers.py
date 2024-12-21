from django.contrib.auth.models import User
from rest_framework import serializers
from postsAPI.models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id','comment', 'username']

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
