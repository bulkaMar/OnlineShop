from django.contrib.auth.models import User
from django.test import TestCase
from accounts.forms import UserLoginForm, UserRegistrationForm, ManagerLoginForm, EditProfileForm


class TestForms(TestCase):
    def test_user_login_form_valid_data(self):
        form = UserLoginForm(data={'email': 'test@example.com', 'password': 'password123'})
        self.assertTrue(form.is_valid())

    def test_user_login_form_no_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
        
