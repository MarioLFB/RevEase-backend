from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterViewTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')
        data = {"username": "newuser", "password": "newpassword", "email": "newuser@example.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)

    def test_register_user_missing_password(self):
        url = reverse('register')
        data = {"username": "newuser", "email": "newuser@example.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
