from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Category, Product
from accounts.models import User


class CartViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', full_name='Test User', password='12345')
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(title='Test Category')
        
        self.product = Product.objects.create(
            price=10,
            category=self.category 
        )

    def test_add_to_cart(self):
        response = self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1})
        self.assertEqual(response.status_code, 302) 

    def test_show_cart(self):
        response = self.client.get(reverse('cart:show_cart'))
        self.assertEqual(response.status_code, 302)

    def test_remove_from_cart(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1})
        response = self.client.post(reverse('cart:remove_from_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302) 
