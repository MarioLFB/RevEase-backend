from rest_framework import viewsets
from .models import Product, Review, Comment, Like, Follower
from .serializers import ProductSerializer, ReviewSerializer, CommentSerializer, LikeSerializer, FollowerSerializer


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer