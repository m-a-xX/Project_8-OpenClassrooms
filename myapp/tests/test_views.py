"""File that contains views tests"""
from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Product, Reg_product, Category
import json


class TestViews(TestCase):
    """Views tests class"""

    def test_index_GET(self):
        """Test homepage view"""
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        
    def test_register_GET(self):
        """Test registration view"""
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        
    def test_credits_GET(self):
        """Test legal mentions view"""
        client = Client()
        response = client.get(reverse('credits'))
        self.assertEquals(response.status_code, 200)
        
    def test_account_GET(self):
        """Test account details view"""
        client = Client()
        response = client.get(reverse('account'))
        self.assertEquals(response.status_code, 200)

    def test_results_GET(self):
        """Test search results view"""
        response = self.client.get('/results/?search=sandwich')
        self.assertEquals(response.status_code, 200)
        
    def test_product_GET(self):
        """Test product details view"""
        client = Client()
        cat = Category.objects.create(
            name='Sandwichs'
        )
        product = Product.objects.create(
            category=cat,
            name='Sandwich au poulet', 
            nutrition_grade = 'a',
            url = 'https://fr.openfoodfacts.org/produit/3560070783038/poulet-curry-carrefour',
            img_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/front_fr.6.400.jpg',
            nut_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/nutrition_fr.7.200.jpg',
        )
        response = self.client.get('/product/?name=Sandwich au poulet')
        self.assertEquals(response.status_code, 200)


    def test_favs_GET(self):
        """Test favorits products view"""
        client = Client()
        response = client.get(reverse('favs'))
        self.assertEquals(response.status_code, 200)
