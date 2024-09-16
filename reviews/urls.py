from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet, CommentViewSet, LikeViewSet, FollowerViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'followers', FollowerViewSet)

urlpatterns = [
    path('', include(router.urls))
]