"""File that contains functions used in views"""
from django.contrib.auth.models import User
from .models import Product, Reg_product


def clean_url(url):
    """Clean the url to return a useable url"""
    url = url.replace("('", '')
    url = url.replace("',)", '')
    return url


def get_attrs(product):
    """Put product's attributs in a tuple"""
    name = product['name']
    cat_id = product['category_id']
    nut_grade = product['nutrition_grade']
    url = clean_url(product['url'])
    img_url = clean_url(product['img_url'])
    nut_url = clean_url(product['nut_url'])
    return (name, cat_id, nut_grade, url, img_url, nut_url)


def get_product(search):
    """Return product attributs"""
    try:
        product = Product.objects.filter(name__icontains=search)[:1].values()
        return get_attrs(product[0])
    except IndexError:
        return None


def get_substituts(cat_id):
    """Find bests products of a category with the category's id"""
    subs = Product.objects.filter(category_id=cat_id).order_by\
           ('nutrition_grade')[:6].values()
    return subs


def exact_product(name):
    """Find a product to return his attributs"""
    product = Product.objects.filter(name__exact=name).values()
    return get_attrs(product[0])


def save_product(product, user):
    """Register a product in the DB and assign this registration to a user"""
    row = Reg_product(product=Product.objects.get(id=product), user=User.\
        objects.get(id=user), nutrition_grade=Product.objects.filter(id=\
        product).values('nutrition_grade')[0]['nutrition_grade'], img_url=\
        Product.objects.filter(id=product).values('img_url')[0]['img_url'], \
        name=Product.objects.filter(id=product).values('name')[0]['name'])
    row.save()


def is_product_reg(product, user):
    """Return a boolean to verify if the product was already saved by the user"""
    test = Reg_product.objects.filter(product=product).filter(user=user)
    if not test:
        return 0
    else:
        return 1


def find_favs(user):
    """Find whats whats products were saved by the user with his id"""
    favs = Reg_product.objects.filter(user=user).values()
    return favs
