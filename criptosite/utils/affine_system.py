# Implementation of Affine Cipher in Python
import utils.globals as g
import numpy as np
# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        quit()
    else:
        return x % m


# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
    '''
	C = (a*P + b) % 26
	'''
    text= g.chartonum(text)
    return ''.join([chr(((key[0] * (t) + key[1]) % 26)+ ord('A')) for t in text])


# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
    '''
	P = (a^-1 * (C - b)) % 26
	'''
    cipher=g.chartonum(cipher)
    return ''.join([chr(((modinv(key[0], 26) * (c - key[1])) % 26) + ord('A')) for c in cipher])

def k(k):
    pk= [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    try:
        t= k.split(",")
        l= [int(x) for x in t]
        K=[]
        gdc= egcd(l[0],l[1])
        if len(l) == 1:
            raise Exception("K invalida")
        elif((l[0] in pk) and (26>l[1]>0) and (gdc[0] == 1)):
            K.append(l[0])
            K.append(l[1])
        else:
            raise Exception("K invalida")
    except:
        t= np.random.randint(1,len(pk))
        K = [pk[t]]
        K.append(pk[np.random.randint(0,t)])
    return K


# Driver Code to test the above functions
def main():
    # declaring text and key
    text = str(input("message: "))#'AFFINE CIPHER'
    tkey = input("key: ") #17,20
    key= k(tkey)
    print(k(tkey))

    # calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format(affine_encrypted_text))

    # calling decryption function
    print('Decrypted Text: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))


if __name__ == '__main__':
    main()
