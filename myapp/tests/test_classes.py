"""File that contains classes tests"""
from django.test import TestCase
from myapp.classes import *
from myapp.models import Product, Category, Reg_product


class TestClasses(TestCase):
    """Classes tests class"""

    def setUp(self):
        """Create category"""
        self.cat = Category.objects.create(
            name='Sandwichs'
        )

    def test_clean_url(self):
        url = "('https://fr.openfoodfacts.org/produit/3560070783038/poulet-curry-carrefour',)"
        res = 'https://fr.openfoodfacts.org/produit/3560070783038/poulet-curry-carrefour'
        self.assertEquals(clean_url(url), res)

    def test_get_attrs(self):
        attrs = {
            'id': 10640,
            'name': 'Nutella',
            'category_id': 89,
            'nutrition_grade': 'e',
            'url': 'https://fr.openfoodfacts.org/produit/80051657/nutella-ferrero',
            'img_url': 'https://static.openfoodfacts.org/images/products/80051657/front_fr.6.400.jpg',
            'nut_url': "('https://static.openfoodfacts.org/images/products/540/024/701/9509/nutrition_fr.9.200.jpg',)"}
        res = ('Nutella', 89, 'e', 'https://fr.openfoodfacts.org/produit/80051657/nutella-ferrero', 'https://static.openfoodfacts.org/images/products/80051657/front_fr.6.400.jpg', 'https://static.openfoodfacts.org/images/products/540/024/701/9509/nutrition_fr.9.200.jpg')
        self.assertEquals(get_attrs(attrs), res)
