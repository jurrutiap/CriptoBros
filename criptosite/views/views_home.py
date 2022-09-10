from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django import forms

import sys
sys.path.append("..")

import utils.shift_system as shift
import utils.multiplicative_system as mp
import utils.sustitutive_system as sus
import utils.vigenere_system as vs

def home(request):
    return render(request, 'index.html')

def shift_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= shift.k(request.POST['k1'])
            data = shift.encrypt(message, k)
            return render(request, 'shift_system.html', {'data':data, 'clear': message, 'k1':k})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= shift.k(request.POST['k2'])
            data = shift.desencrypt(message, k)
            return render(request, 'shift_system.html', {'data':data, 'cipher': message, 'k2':k})

    return render(request, 'shift_system.html')

def multiplicative_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= mp.k(request.POST['k1'])
            data = mp.encrypt(message, k)
            return render(request, 'multiplicative_system.html', {'data':data, 'clear': message, 'k1':k})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= mp.k(request.POST['k2'])
            data = mp.desencrypt(message, k)
            return render(request, 'multiplicative_system.html', {'data':data, 'cipher': message, 'k2':k})

    return render(request, 'multiplicative_system.html')

def sustitutive_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= sus.k(request.POST['k1'], message)
            data = sus.encrypt(k, message)
            return render(request, 'sustitutive_system.html', {'data':data, 'clear': message, 'k1':k})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= sus.k(request.POST['k2'], message)
            data = sus.desencrypt(k, message)
            return render(request, 'sustitutive_system.html', {'data':data, 'cipher': message, 'k2':k})

    return render(request, 'sustitutive_system.html')

def vigenere_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= vs.generateKey(message, request.POST['k1'])
            data = vs.cipherText(message, k)
            return render(request, 'vigenere_system.html', {'data':data, 'clear': message, 'k1':k})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= vs.generateKey(message, request.POST['k2'])
            data = vs.DecryptedText(message, k)
            return render(request, 'vigenere_system.html', {'data':data, 'cipher': message, 'k2':k})

    return render(request, 'vigenere_system.html')