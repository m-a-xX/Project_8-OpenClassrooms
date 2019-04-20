"""Import the products and create the DB
To run in the Django shell : exec(open('myapp/products.py').read())"""
import requests
from myapp.models import Category, Product, Reg_product

CATS = ['Préparations de viande hachée', 'Pizzas surgelées', 'Yaourts',
        'Biscuits', 'Fromages', 'Chips', 'Compotes', 'Biscuits apéritifs',
        'Fruits secs', 'Plats préparés en conserve', 'Thons', 'Sandwichs',
        'Salades composées', 'Plantes condimentaires', 'Mueslis croustillants', 
        'Nouilles', 'Mueslis croustillants', 'Céréales soufflées', 'Pâtisseries',
        'Céréales fourées', 'Desserts glacés', 'Soupes de légumes', 'Filets \
        de poissons', 'Barres chocolatées', 'Bonbons gélifiés', 'Tapenades',
        'Pâtes à tartiner', 'Poulets cuisinés', 'Tartes', 'Légumes frais'
        'Filets de poulet', 'Ailes de poulet', 'Viandes séchées', 'Graines',
        'Produits de la ruche', 'Saumons', 'Tomates et dérivés', 'Pâtes farcies',
        'Gâteaux au chocolat', 'Sardines', 'Milkfat', 'Olives', 'Charcuteries cuites',
        'Steaks', 'Légumes secs', 'Plats au porc', 'Crêpes et galettes',
        'Confitures de fraises', 'Rillettes de poissons', 'Veloutés de légumes',
        'Cacaos et chocolats en poudre', 'Taboulés', 'Panettone', 'Crustacés',
        'Boudin', 'Sauces pour pâtes', 'Purées', 'Gaufres', 'Gratins',
        'Soupes de poissons', 'Houmous', 'Ketchup', 'Nougats']

def load_products():
    '''Import products from API and add them in the database'''
    nbr = 0
    for i in range(0, len(CATS)):
        cat = Category(name=CATS[i])
        cat.save()
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': CATS[i],
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
                except KeyError as e:
                    try:
                        name = product['product_name']
                    except KeyError as e:
                        pass
                try:
                    nutrition_grade = product['nutrition_grade_fr']
                except KeyError as e:
                    try:
                        nutrition_grade = product['nutrition_grade']
                    except KeyError as e:
                        pass
                url = product['url']
                image = product['image_front_url']
                try:
                    nutrition_image = product["image_nutrition_small_url"], 
                    atts = (nbr, name, CATS[i], nutrition_grade, url, image, i,
                            nutrition_image)
                except KeyError as e:
                    atts = (nbr, name, CATS[i], nutrition_grade, url, image, i)
                name = name.replace("\n", " ")
                name = name.replace("&#39;", "'")
                product = Product(name = name, category = cat, \
                                  nutrition_grade = nutrition_grade, url = url, \
                                  img_url = image, nut_url = nutrition_image)
                nbr += 1
                product.save()
        except KeyError as e:
            pass

def del_duplicate():
    for row in Product.objects.all():
        if Product.objects.filter(name=row.name).count() > 1:
            row.delete()
    for row in Product.objects.all():
        if Product.objects.filter(name__iexact=row.name).count() > 1:
            row.delete()

load_products()
del_duplicate()