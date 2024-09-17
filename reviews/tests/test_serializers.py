from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Product, Review
from ..serializers import ProductSerializer, ReviewSerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name="Test Product", description="A product for testing", category="Testing", price=9.99, owner=self.user)
        self.serializer = ProductSerializer(instance=self.product)

    def test_product_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.product.name)
        self.assertEqual(data['owner'], self.user.username)

class ReviewSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name="Test Product", description="A product for testing", category="Testing", price=9.99, owner=self.user)
        self.review = Review.objects.create(content="Great product!", rating=5, product=self.product, author=self.user)
        self.serializer = ReviewSerializer(instance=self.review)

    def test_review_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['content'], self.review.content)
        self.assertEqual(data['rating'], self.review.rating)
