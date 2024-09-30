from rest_framework import serializers
from .models import Product, Review, Comment, Like, Follower
from django.contrib.auth.models import User

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
    review = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'review', 'author']

    def create(self, validated_data):
        user = self.context['request'].user
        review = validated_data['review']
        existing_like = Like.objects.filter(author=user, review=review).first()
        if existing_like:
            raise serializers.ValidationError({'detail': 'Você já curtiu esta review.'})
        return Like.objects.create(author=user, review=review)

# Follower Serializer
class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following']
