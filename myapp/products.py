"""Import the products and create the DB
To run in the Django shell : exec(open('myapp/products.py').read())"""
import requests
from myapp.models import Category, Product

CATS = ['Préparations de viande hachée', 'Pizzas surgelées', 'Yaourts',
        'Biscuits', 'Fromages', 'Chips', 'Compotes', 'Biscuits apéritifs',
        'Fruits secs', 'Plats préparés en conserve', 'Thons', 'Sandwichs',
        'Salades composées', 'Plantes condimentaires', 'Mueslis croustillants',
        'Nouilles', 'Mueslis croustillants', 'Céréales soufflées',
        'Céréales fourées', 'Desserts glacés', 'Soupes de légumes', 'Filets \
        de poissons', 'Barres chocolatées', 'Bonbons gélifiés', 'Tapenades',
        'Pâtes à tartiner', 'Poulets cuisinés', 'Tartes', 'Légumes frais'
        'Filets de poulet', 'Ailes de poulet', 'Viandes séchées', 'Graines',
        'Produits de la ruche', 'Saumons', 'Tomates et dérivés',
        'Gâteaux au chocolat', 'Sardines', 'Milkfat', 'Olives',
        'Steaks', 'Légumes secs', 'Plats au porc', 'Crêpes et galettes',
        'Confitures de fraises', 'Rillettes de poissons',
        'Cacaos et chocolats en poudre', 'Taboulés', 'Panettone', 'Crustacés',
        'Boudin', 'Sauces pour pâtes', 'Purées', 'Gaufres', 'Gratins',
        'Soupes de poissons', 'Houmous', 'Ketchup', 'Nougats', 'Pâtisseries',
        'Pâtes farcies', 'Charcuteries cuites', 'Veloutés de légumes']

def load_products():
    '''Import products from API and add them in the database'''
    nbr = 0
    for category in CATS:
        try:
            cat = Category.objects.get(name=category)
        except:
            cat = Category(name=category)
            cat.save()
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'countries': 'France',
            'page_size': '250',
            'json': 1
            }
        reponse = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', \
                               params=payload)
        data = reponse.json()
        try:
            for product in data['products']:
                try:
                    name = product['product_name_fr']
                except KeyError:
                    try:
                        name = product['product_name']
                    except KeyError:
                        pass
                try:
                    nutrition_grade = product['nutrition_grade_fr']
                except KeyError:
                    try:
                        nutrition_grade = product['nutrition_grade']
                    except KeyError:
                        pass
                url = product['url']
                image = product['image_front_url']
                try:
                    nutrition_image = product["image_nutrition_small_url"]
                except KeyError:
                    pass
                name = name.replace("\n", " ")
                name = name.replace("&#39;", "'")
                try:
                    product = Product.objects.get(name=name, category=cat)
                except:
                    product = Product(name=name, category=cat, \
                                    nutrition_grade=nutrition_grade, url=url,\
                                    img_url=image, nut_url=nutrition_image)
                    nbr += 1
                    product.save()
        except KeyError:
            pass

def del_duplicate():
    """Delete multiple records of a same product"""
    for row in Product.objects.all():
        if Product.objects.filter(name=row.name).count() > 1:
            row.delete()
    for row in Product.objects.all():
        if Product.objects.filter(name__iexact=row.name).count() > 1:
            row.delete()

load_products()
del_duplicate()
