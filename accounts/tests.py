import pytest
from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User


# Create your tests here.
class TestPagesViews(TestCase):

    def test_login_view_status(self):
        client = Client()
        url = reverse("login")
        response = client.get(url)
        assert response.status_code == 200
    
    def test_register_view_status(self):
        client = Client()
        url = reverse("register")
        response = client.get(url)
        assert response.status_code == 200


class LogInTest(TestCase):

    def setUp(self):
        self.credentials  = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        User.objects.create_user(**self.credentials )

    def test_login(self):
        client = Client()
        logged_in = client.login(**self.credentials)
        self.assertTrue(logged_in)

#TODO: Test for register