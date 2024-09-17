from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Product, Review, Comment, Like, Follower

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(
            name="Test Product",
            description="A product for testing",
            category="Testing",
            price=9.99,
            owner=self.user
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.owner.username, 'testuser')

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name="Test Product", description="A product for testing", category="Testing", price=9.99, owner=self.user)
        self.review = Review.objects.create(content="Great product!", rating=5, product=self.product, author=self.user)

    def test_review_creation(self):
        self.assertEqual(self.review.content, "Great product!")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.product.name, "Test Product")
