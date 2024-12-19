from django.shortcuts import render
from rest_framework import viewsets
from postsAPI.models import Post
from postsBackend.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
