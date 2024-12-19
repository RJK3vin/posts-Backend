from postsAPI import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postsAPI.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls))
]