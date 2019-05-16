"""File that contain views associates to urls"""
from django.contrib import admin
from django.urls import path, include
from myapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', v.register, name='register'),
    path('credits/', v.legal_mentions, name='credits'),
    path('account/', v.account, name='account'),
    path('results/', v.results, name='results'),
    path('product/', v.product, name='product'),
    path('reg_product/', v.reg_product, name='reg_product'),
    path('favs/', v.favs, name='favs'),
]
