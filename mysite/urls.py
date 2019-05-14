"""File that contain views associates to urls"""
from django.contrib import admin
from django.urls import path, include, re_path
from myapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', v.register, name='register'),
    path('credits/', v.legal_mentions, name='credits'),
    path('profil/', v.profil, name='profil'),
    path('results/', v.results, name='results'),
    path('product/', v.product, name='product'),
    path('reg_product/', v.reg_product, name='reg_product'),
    path('favorites/', v.favorites, name='favorites'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate, name='activate'),
]
