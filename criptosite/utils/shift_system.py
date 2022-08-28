import numpy as np
import globals as g

def k():
    try:
        K= int(input())%26
        print(K)
    except:
        K = np.random.randint(26)
        print("Se eligio una clave random")
        print(K)
    return K

def encrypt(text, K):
    listcrypt= []
    x= g.chartonum(text)
    for i in x:
        listcrypt.append((i+K)%26)
    return g.numtochar(listcrypt)

def desencrypt(text, K):
    listcrypt= []
    x= g.chartonum(text)
    for i in x:
        listcrypt.append((i-K)%26)
    return g.numtochar(listcrypt)
