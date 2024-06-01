from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm, ManagerLoginForm, EditProfileForm
from accounts.views import create_manager


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='test@example.com',
            full_name='Test User',
            password='testpassword'
        )

    def test_create_manager(self):
        create_manager()
        manager = User.objects.get(email="manager@example.com")
        self.assertTrue(manager.is_manager)

    def test_manager_login_view(self):
        response = self.client.get(reverse('accounts:manager_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manager_login.html')

        response = self.client.post(reverse('accounts:manager_login'), {
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302) 

    def test_user_register_view(self):
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        response = self.client.post(reverse('accounts:user_register'), {
            'email': 'newuser@example.com',
            'full_name': 'New User',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302) 


    def test_edit_profile_view(self):
        self.client.login(email='test@example.com', password='testpassword')

        response = self.client.get(reverse('accounts:edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

        response = self.client.post(reverse('accounts:edit_profile'), {
            'full_name': 'Updated User Name',
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 302)
