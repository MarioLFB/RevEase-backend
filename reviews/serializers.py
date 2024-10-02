from rest_framework import serializers
from .models import Product, Review, Comment, Follower
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'created_at', 'owner']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'created_at', 'product', 'author', 'comments']

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(comments, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    review = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'review', 'author']


class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following']
