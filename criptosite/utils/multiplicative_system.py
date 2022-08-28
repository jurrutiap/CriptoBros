import math as m
import numpy as np
import globals as g

def k():
    control= True
    while control:
        try:
            K= int(input())%26
            if m.gcd(K,26) == 1:
                print(K)
                control = False
            else:
                pass
        except:
            x= [3,5,7,9,11,15,17,19,21,23,25]
            y= np.random.randint(len(x))
            K = x[y]
            print("Se eligio una clave random")
            print(K)
            control = False
    return K

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def encrypt(text, K):
    listcrypt= []
    x= g.chartonum(text)
    for i in x:
        listcrypt.append((K*i)%26)
    return g.numtochar(listcrypt)

def desencrypt(text, K):
    gdc, s, y = extended_gcd(K, 26)
    listcrypt= []
    x= g.chartonum(text)
    for i in x:
        listcrypt.append((i*s)%26)
    return g.numtochar(listcrypt)
    