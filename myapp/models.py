"""File that contains tables used in the DB"""
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Category(models.Model):
    """Table it contains categories"""
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Product(models.Model):
    """Table it contains products"""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    nut_url = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Reg_product(models.Model):
    """Table it contains saved products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    nutrition_grade = models.CharField(max_length=1)
    img_url = models.CharField(max_length=200)
