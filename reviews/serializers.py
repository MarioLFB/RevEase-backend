from rest_framework import serializers
from .models import Product, Review, Comment, Like, Follower


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'created_at', 'owner'] 


# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'created_at', 'product', 'author']


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'review', 'author']


# Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'review', 'author']


# Follower Serializer
class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following']
