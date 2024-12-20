from django.shortcuts import render
from rest_framework import viewsets
from postsAPI.models import Post
from postsBackend.serializers import PostSerializer, UserSerializer, UserCreateSerializer
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCreateView(APIView):
    def post(self, request):
        serliazer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serliazer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
