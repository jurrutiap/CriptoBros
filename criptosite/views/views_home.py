from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django import forms
from django.core.files.storage import FileSystemStorage

import os
import sys
import mimetypes
import time
sys.path.append("..")

import utils.shift_system as shift
import utils.multiplicative_system as mp
import utils.sustitutive_system as sus
import utils.vigenere_system as vs
import utils.substitution_system as sb
import utils.shift_crypto_analisis as shiftA
import utils.Vigenere_Cryptoanalisys as vigenereA
import utils.affine_Cryptoanalisys as affineA
import utils.affine_system as afs
import utils.hill_image_system as his
import utils.Substitution_Cryptoanalisys as susan
import utils.gammaPentagonal as gp
import utils.DES as DES
import utils.DESImage as DESi
import utils.AES as AES 

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

def substitution_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= sb.k(request.POST['k1'])
            data = sb.cipher_text(message, k)
            return render(request, 'substitution_system.html', {'data':data, 'clear': message, 'k1':k})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= sb.k(request.POST['k2'])
            data = sb.DecryptedText(message, k)
            return render(request, 'substitution_system.html', {'data':data, 'cipher': message, 'k2':k})

    return render(request, 'substitution_system.html')

def affine_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= afs.k(request.POST['k1'])
            data = afs.affine_encrypt(message, k)
            return render(request, 'affine_system.html', {'data':data, 'clear': message, 'k1':'%i,%i'%(k[0],k[1])})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= afs.k(request.POST['k2'])
            data = afs.affine_decrypt(message, k)
            return render(request, 'affine_system.html', {'data':data, 'cipher': message, 'k2':request.POST['k2']})

    return render(request, 'affine_system.html')

def gammaPentagonal_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            data = gp.encryptGammaPentagonal(message)
            return render(request, 'gamapentagonal_system.html', {'data':data, 'clear': message})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= afs.k(request.POST['k2'])
            data = gp.decryptGammaPentagonal(message, k)
            return render(request, 'gamapentagonal_system.html', {'data':data, 'cipher': message, 'k2':request.POST['k2']})

    return render(request, 'gamapentagonal_system.html')

def DES_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            k= DES.K(request.POST['k1'])
            data = DES.DESEncrypt(message, k)
            return render(request, 'DES_system.html', {'data':data[0], 'clear': message, 'k1':k})

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= DES.K(request.POST['k2'])
            data = DES.DESDecrypt(message, k)
            return render(request, 'DES_system.html', {'data':data[0], 'cipher': message, 'k2':request.POST['k2']})
    return render(request, 'DES_system.html')

def hill_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            if os.path.exists("criptosite/static/img/clean.png"):
                os.remove("criptosite/static/img/clean.png")
            upload = request.FILES['im1']
            fss = FileSystemStorage()
            fss.save('criptosite/static/img/clean.png', upload)
            his.encrypt_img()
            return render(request, 'hill_system.html', {'encrypted_image':'aaaaa'})

        if 'decrypt' in request.POST:
            if os.path.exists("criptosite/static/img/Key.png"):
                os.remove("criptosite/static/img/Key.png")
                os.remove("criptosite/static/img/Encrypted.png")
            fss = FileSystemStorage()
            upload = request.FILES['im2']
            fss.save('criptosite/static/img/Encrypted.png', upload)
            upload = request.FILES['key']
            fss.save('criptosite/static/img/Key.png', upload)
            his.decript_img()
            time.sleep(5)
            return render(request, 'hill_system.html', {'decrypted_image':'aaaaa'})

    return render(request, 'hill_system.html')

def DESimage_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            if os.path.exists("criptosite/static/img/clean.png"):
                os.remove("criptosite/static/img/clean.png")
            upload = request.FILES['im1']
            k= request.POST['k1']
            fss = FileSystemStorage()
            fss.save('criptosite/static/img/clean.png', upload)
            k= DESi.encryptDESImage(k)
            return render(request, 'DESimage_system.html', {'encrypted_image':'aaaaa', 'k1':k})

        if 'decrypt' in request.POST:
            if os.path.exists("criptosite/static/img/Encrypted.png"):
                os.remove("criptosite/static/img/Encrypted.png")
            fss = FileSystemStorage()
            k= request.POST['k2']
            upload = request.FILES['im2']
            fss.save('criptosite/static/img/Encrypted.png', upload)
            k= DESi.decryptDESImage(k)
            time.sleep(5)
            return render(request, 'DESimage_system.html', {'decrypted_image':'aaaaa', 'k2':k})

    return render(request, 'DESimage_system.html')

def AESimage_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            if os.path.exists("criptosite/static/img/AES/AES_image.png"):
                os.remove("criptosite/static/img/AES/AES_image.png")
            upload = request.FILES['im1']
            fss = FileSystemStorage()
            fss.save('criptosite/static/img/clean.png', upload)
            his.encrypt_img()
            return render(request, 'AES.html', {'encrypted_image':'aaaaa'})
        if 'decrypt' in request.POST:
            if os.path.exists("criptosite/static/img/Key.png"):
                os.remove("criptosite/static/img/Key.png")
                os.remove("criptosite/static/img/Encrypted.png")
            fss = FileSystemStorage()
            upload = request.FILES['im2']
            fss.save('criptosite/static/img/Encrypted.png', upload)
            upload = request.FILES['key']
            fss.save('criptosite/static/img/Key.png', upload)
            his.decript_img()
            time.sleep(5)
            return render(request, 'AES.html', {'decrypted_image':'aaaaa'})
    return render(request, 'AES.html')


def shiftcryptoanalisis_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            data = shiftA.ShiftCipherCryptanalysis(message)
            return render(request, 'shift_crypto_analisis.html', {'clear': message})

    return render(request, 'shift_crypto_analisis.html')

def vigenerecryptoanalisis_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            vigenereA.VigenereCryptoanalisys(message)
            return render(request, 'vigenere_crypto_analisis.html', {'clear': message})

    return render(request, 'vigenere_crypto_analisis.html')

def affinecryptoanalisis_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            affineA.AffineCryptoanalisys(message)
            return render(request, 'affine_crypto_analisis.html', {'clear': message})

    return render(request, 'affine_crypto_analisis.html')

def substitutioncryptoanalisis_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            susan.SubstitutionCryptoanalisys(message)
            return render(request, 'substitution_crypto_analisis.html', {'clear': message})

    return render(request, 'substitution_crypto_analisis.html')


def download_file(request):
    # Define text file name
    filename = 'utils/results.txt'
    # Open the file for reading content
    path = open(filename, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filename)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def downloadimg_file(request):
    # Define text file name
    filename = 'criptosite/static/img/Encrypted.png'
    # Open the file for reading content
    path = open(filename, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filename)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def downloadimge_file(request):
    # Define text file name
    filename = 'criptosite/static/img/Decrypted.png'
    # Open the file for reading content
    path = open(filename, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filename)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response