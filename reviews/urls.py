from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ProductViewSet, ReviewViewSet, CommentViewSet, FollowerViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'followers', FollowerViewSet)

reviews_router = routers.NestedDefaultRouter(router, r'reviews', lookup='review')
reviews_router.register(r'comments', CommentViewSet, basename='review-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(reviews_router.urls)),
]
