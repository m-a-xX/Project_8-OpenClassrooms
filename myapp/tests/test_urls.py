"""File that contains urls tests"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from myapp.views import *


class TestUrls(SimpleTestCase):
    """Urls tests class"""

    def test_homepage_url_is_resolved(self):
        """Test the homepage url"""
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_register_url_is_resolved(self):
        """Test the registration page url"""
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_credits_url_is_resolved(self):
        """Test the credits url"""
        url = reverse('credits')
        self.assertEquals(resolve(url).func, legal_mentions)

    def test_account_url_is_resolved(self):
        """Test the account page url"""
        url = reverse('profil')
        self.assertEquals(resolve(url).func, profil)

    def test_results_url_is_resolved(self):
        """Test the results page url"""
        url = reverse('results')
        self.assertEquals(resolve(url).func, results)

    def test_product_url_is_resolved(self):
        """Test the product details page url"""
        url = reverse('product')
        self.assertEquals(resolve(url).func, product)

    def test_reg_product_url_is_resolved(self):
        """Test the reg_product url"""
        url = reverse('reg_product')
        self.assertEquals(resolve(url).func, reg_product)

    def test_favs_url_is_resolved(self):
        """Test the favorits products url"""
        url = reverse('favorites')
        self.assertEquals(resolve(url).func, favorites)
