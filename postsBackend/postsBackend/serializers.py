from django.contrib.auth.models import User
from rest_framework import serializers
from postsAPI.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['comments']
