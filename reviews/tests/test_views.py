from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import Product, Review

class ProductViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product_data = {'name': 'Test Product', 'description': 'A product for testing', 'category': 'Testing', 'price': '9.99'}
        
    def test_create_product(self):
        response = self.client.post('/api/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Test Product')

    def test_get_products(self):
        Product.objects.create(name="Test Product", description="A product for testing", category="Testing", price=9.99, owner=self.user)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

class ReviewViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name="Test Product", description="A product for testing", category="Testing", price=9.99, owner=self.user)
        self.review_data = {'content': 'Great product!', 'rating': 5, 'product': self.product.id}
        
    def test_create_review(self):
        response = self.client.post('/api/reviews/', self.review_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['content'], 'Great product!')

    def test_get_reviews(self):
        Review.objects.create(content="Great product!", rating=5, product=self.product, author=self.user)
        response = self.client.get('/api/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)