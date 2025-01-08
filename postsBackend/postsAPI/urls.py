from postsAPI import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postsAPI.views import PostViewSet, UserCreateView, UserListView, CommentListView, CommentCreateView
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include(router.urls)),
    path('users/me/', views.UserProfileView.as_view(), name='user-profile'),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('posts/<int:post_id>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
]