from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, render_to_response
from myapp.classes import get_product, get_substituts, exact_product, save_product, is_product_reg
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
        substituts = get_substituts(product[1])
        subs = substituts
        paginator = Paginator(subs, 6)
        page = request.GET.get('page')
        subs = paginator.get_page(page)
        user = request.user
        is_reg = {}
        for sub in substituts:
            is_reg[sub['id']] = is_product_reg(sub['id'], user.id)
        context = {
            'name': product[0],
            'img_url': product[4],
            'subs': subs,
            'is_reg': is_reg
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
    product = int(request.GET.get('id', ''))
    user = request.user
    save_product(product, user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
