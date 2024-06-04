from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Category, Product
import json

class TestViews(TestCase):
    def test_home_page(self):
        client=Client()
        response = client.get(reverse('shop:home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_favourites(self):
        client=Client()
        response = client.get(reverse('shop:favorites'))
        self.assertEqual(response.status_code, 302)

