import pytest
from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import SignUpForm


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

class SignUpTest(TestCase):

    """ Test for everything alright """
    def test_sign_up_success(self):

        data = {
            'username': 'testinguser',
            'email': 'test@example.com',
            'password1': 'Polska321@',
            'password2': 'Polska321@'
        }

        form = SignUpForm(data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.non_field_errors(), [])


    """ Test for password too similar to username """
    def test_sign_up_fail(self):

        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'test1',
            'password2': 'test2'
        }

        form = SignUpForm(data)

        self.assertFalse(form.is_valid())