from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Category, Product
from accounts.models import User
from django.urls import reverse

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', full_name='Test User', password='12345')
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(title='Test Category')

        self.product = Product.objects.create(
            price=100,
            category=self.category
        )

    def test_add_to_favorites(self):
        response = self.client.post(reverse('shop:add_to_favorites', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

    def test_remove_from_favorites(self):
        response = self.client.post(reverse('shop:remove_from_favorites', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)