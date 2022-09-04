from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django import forms

import sys
sys.path.append("..")

from utils.shift_system import encrypt, desencrypt

def home(request):
    return render(request, 'index.html')

def sistema1(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            data = encrypt(message, 1)
            return render(request, 'shift_system.html', {'data':data, 'clear': message})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            data = desencrypt(message, 1)
            return render(request, 'shift_system.html', {'data':data, 'cipher': message})

    return render(request, 'shift_system.html')