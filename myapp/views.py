from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login
from myapp.forms import RegistrationForm, SearchForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SearchForm()
    context = {'form' : form}
    return render(request, 'index.html', context)


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
