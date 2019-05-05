"""Views called in urls"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from myapp.forms import RegistrationForm
from myapp.classes import get_product, get_substituts, exact_product, \
     save_product, is_product_reg, find_favs
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def index(request):
    """Home page"""
    return render(request, 'index.html')


def legal_mentions(request):
    """Credits pages"""
    return render(request, 'credits.html')


def account(request):
    """Active user account informations page"""
    return render(request, 'account.html')


def register(request):
    """Registartion page"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
    		'user': user,
    		'domain': current_site.domain,
    		'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
    		'token': account_activation_token.make_token(user),
	    })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            context = {
                'message': "Veuillez confirmer votre adresse mail pour finaliser l'inscription."
            }
            return render(request, 'registration/register.html', context)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        context = {
            'error': "Votre compte est maintenant activé."
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponse('Activation link is invalid!')

def results(request):
    """Results of search"""
    search = request.GET.get('search')
    search_product = get_product(search)
    if search_product is None:
        context = {
            'error': "Nous n'avons pas réussi à trouver le produit que vous \
            souhaitez remplacer."
        }
        return render(request, 'index.html', context)
    else:
        substituts = get_substituts(search_product[1])
        subs = substituts
        paginator = Paginator(subs, 6)
        page = request.GET.get('page')
        subs = paginator.get_page(page)
        user = request.user
        is_reg = {}
        for sub in substituts:
            is_reg[sub['id']] = is_product_reg(sub['id'], user.id)
        context = {
            'name': search_product[0],
            'img_url': search_product[4],
            'subs': subs,
            'is_reg': is_reg
        }
        return render(request, 'results.html', context)


def product(request):
    """Product details page"""
    try:
        name = request.GET.get('name', '')
        product_attrs = exact_product(name)
        context = {
            'name': product_attrs[0],
            'cat_id': product_attrs[1],
            'nut': product_attrs[2],
            'url': product_attrs[3],
            'img_url': product_attrs[4],
            'nut_url': product_attrs[5],
        }
        return render(request, 'product.html', context)
    except IndexError:
        name = request.GET.get('name', '')
        name = (name + ' ')
        product_attrs = exact_product(name)
        context = {
            'name': product_attrs[0],
            'cat_id': product_attrs[1],
            'nut': product_attrs[2],
            'url': product_attrs[3],
            'img_url': product_attrs[4],
            'nut_url': product_attrs[5],
        }
        return render(request, 'product.html', context)


def reg_product(request):
    """Retreive product id and user id and call the function to save te product"""
    product_id = int(request.GET.get('id', ''))
    user = request.user
    save_product(product_id, user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def favs(request):
    """Print products saved by active user"""
    user = request.user
    favorits = find_favs(user.id)
    paginator = Paginator(favorits, 6)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1
    pag = paginator.get_page(page)
    context = {
        'favs': pag,
        'len': len(pag),
    }
    return render(request, 'favs.html', context)
