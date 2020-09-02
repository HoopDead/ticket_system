import pytest
from django.urls import reverse, resolve
from django.test import TestCase, Client

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