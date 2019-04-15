import psycopg2
from .models import Product, Category, Reg_product

def clean_url(url):
    url = url.replace("('", '')
    url = url.replace("',)", '')
    return url

def get_attrs(product):
    name = product['name']
    cat_id = product['category_id']
    nut_grade = product['nutrition_grade']
    url = clean_url(product['url'])
    img_url = clean_url(product['img_url'])
    nut_url = clean_url(product['nut_url'])
    return (name, cat_id, nut_grade, url, img_url, nut_url)

def get_product(search):
    try:
        product = Product.objects.filter(name__icontains = search)[:1].values()
        return get_attrs(product[0])
    except IndexError:
        return None

def get_substituts(cat_id):
    subs = Product.objects.filter(category_id = cat_id).order_by('nutrition_grade')[:6].values()
    return subs

def exact_product(name):
    product = Product.objects.filter(name__exact = name).values()
    return get_attrs(product[0])