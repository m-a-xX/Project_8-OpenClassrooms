from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, render_to_response
from myapp.classes import get_product, get_substituts, exact_product
from myapp.forms import RegistrationForm, SearchForm
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')

def credits(request):
    return render(request, 'credits.html')

def account(request):
    return render(request, 'account.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def results(request):
    search = request.GET.get('search')
    product = get_product(search)
    if product == None:
        context = {
            'error': "Nous n'avons pas réussi à trouver le produit que vous souhaitez remplacer."
        }
        return render(request, 'index.html', context)
    else:
        subs = get_substituts(product[1])
        paginator = Paginator(subs, 6)
        page = request.GET.get('page')
        subs = paginator.get_page(page)
        context = {
            'name': product[0],
            'img_url': product[4],
            'subs': subs
        }
        return render(request, 'results.html', context)

def product(request):
    try:
        name = request.GET.get('name', '')
        product = exact_product(name)
        context = {
            'name': product[0],
            'cat_id': product[1],
            'nut': product[2],
            'url': product[3],
            'img_url': product[4],
            'nut_url': product[5],
        }
        return render(request, 'product.html', context)
    
    except IndexError:
        name = request.GET.get('name', '')
        name = (name + ' ')
        print(name)
        product = exact_product(name)
        context = {
            'name': product[0],
            'cat_id': product[1],
            'nut': product[2],
            'url': product[3],
            'img_url': product[4],
            'nut_url': product[5],
        }
        return render(request, 'product.html', context)

def reg_product(request):
    return render(request, 'results.html')