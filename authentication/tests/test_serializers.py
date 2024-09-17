from django.test import TestCase
from authentication.serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterSerializerTests(TestCase):

    def test_valid_data_creates_user(self):
        data = {"username": "testuser", "password": "testpassword", "email": "testuser@example.com"}
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, "testuser")

    def test_missing_password(self):
        data = {"username": "testuser", "email": "testuser@example.com"}
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
