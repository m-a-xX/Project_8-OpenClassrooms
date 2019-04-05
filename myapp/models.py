from django.db import models
#from .products import CATS, load_products
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition_grade = models.CharField(max_length = 1)
    url = models.CharField(max_length = 200)
    img_url = models.CharField(max_length = 200)
    nut_url = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Reg_product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    nutrition_grade = models.CharField(max_length = 1)
    url = models.CharField(max_length = 200)
    img_url = models.CharField(max_length = 200)
    nut_url = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
