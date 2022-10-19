from pyDes import des, CBC, PAD_PKCS5
import binascii
import utils.globals as g
import numpy as np


def K(key):
    try:
        if len(key) == 8:
            return key
        else:
            raise Exception("La clave es mas grande que el texto")
    except:
        y= []
        for i in range(8):
            y.append(np.random.randint(26))
        key = g.numtochar(y)
        return key



def DESEncrypt(s, key):
    """
         Cifrado DES
         : param s: cadena sin procesar
         : return: cadena encriptada, hexadecimal
    """
    secret_key = key
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    e= str(binascii.b2a_hex(en))[2:-1]
    return e, key


def DESDecrypt(s, key):
    """
         Descifrado DES
         : param s: cadena encriptada, hexadecimal
         : return: cadena descifrada
    """
    secret_key = key
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    d= str(de)[2:-1]
    return d, key

