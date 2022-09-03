from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def sistema1(request):
    return render(request, 'tables.html')
