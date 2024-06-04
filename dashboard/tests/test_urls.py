from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import add_product,add_category, orders
class TestUrls(SimpleTestCase):

    def test_add_category_url(self):
        url = reverse('dashboard:add_category')
        print(url)
        self.assertEqual(resolve(url).func, add_category)

    def test_add_product_url(self):
        url = reverse('dashboard:add_product')
        print(url)
        self.assertEqual(resolve(url).func, add_product)

    def test_orders_url(self):
        url = reverse('dashboard:orders')
        print(url)
        self.assertEqual(resolve(url).func, orders)