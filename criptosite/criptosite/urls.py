"""criptosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views.views_home import home, shift_view, multiplicative_view, sustitutive_view, vigenere_view, substitution_view, shiftcryptoanalisis_view, vigenerecryptoanalisis_view, affine_view, download_file

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('shift/', shift_view, name='shift_view'),
    path('multiplicative/', multiplicative_view, name='multiplicative_view'),
    path('sustitutive/', sustitutive_view, name='sustitutive_view'),
    path('vigenere/', vigenere_view, name='vigenere_view'),
    path('substitution/', substitution_view, name='substitution_view'),
    path('shiftcryptoanalisis/', shiftcryptoanalisis_view, name='shiftcryptoanalisis_view'),
    path('vigenerecryptoanalisis/', vigenerecryptoanalisis_view, name='vigenerecryptoanalisis_view'),
    path('affine/', affine_view, name='affine_view'),
    path('download/', download_file, name='download_file'),
]
urlpatterns += staticfiles_urlpatterns()