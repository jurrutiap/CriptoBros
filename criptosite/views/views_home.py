from ..utils.shift_system import encrypt

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def sistema1(request):
    return render(request, 'charts.html')

def shift(request, message, K):
    if request.method == "POST":
        data = encrypt(message, K)
        return render(request, 'charts.html', {'data':data})
