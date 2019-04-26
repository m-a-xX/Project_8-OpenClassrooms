"""File that contains models tests"""
from django.test import TestCase
from django.contrib.auth.models import User
from myapp.models import Product, Category, Reg_product


class TestModels(TestCase):
    """Models tests class"""

    def setUp(self):
        """Create category"""
        self.cat = Category.objects.create(
            name='Sandwichs'
        )

    def test_category_creation(self):
        """Test category creation"""
        self.assertEquals(self.cat.name, 'Sandwichs')

    def test_product_creation(self):
        """Test product creation"""
        product = Product.objects.create(
            category=self.cat,
            name='Sandwich au poulet', 
            nutrition_grade = 'a',
            url = 'https://fr.openfoodfacts.org/produit/3560070783038/poulet-curry-carrefour',
            img_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/front_fr.6.400.jpg',
            nut_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/nutrition_fr.7.200.jpg',
        )
        self.assertEquals(Product.objects.filter(id=1).values('name')[0]['name'], 'Sandwich au poulet')

    def test_reg_product_creation(self):
        """Test product registration"""
        product = Product.objects.create(
            id=1,
            category=self.cat,
            name='Sandwich au poulet', 
            nutrition_grade = 'a',
            url = 'https://fr.openfoodfacts.org/produit/3560070783038/poulet-curry-carrefour',
            img_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/front_fr.6.400.jpg',
            nut_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/nutrition_fr.7.200.jpg',
        )
        user = User.objects.create(
            username='user',
            id='1',
        )
        reg_product = Reg_product.objects.create(
            name='Sandwich au poulet',
            product_id=1,
            user=user,
            nutrition_grade = 'a',
            img_url = 'https://static.openfoodfacts.org/images/products/356/007/078/3038/front_fr.6.400.jpg',
        )
        self.assertEquals(Reg_product.objects.filter(id=1).values('name')[0]['name'], 'Sandwich au poulet')