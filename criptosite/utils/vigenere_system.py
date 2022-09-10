import utils.globals as g
import numpy as np


def generateKey(string, key):
    try:
        if key == '':
            raise Exception("La clave es mas grande que el texto")
        elif len(string) > len(key):
            key = list(key)
            return "".join(key)
        else:
            raise Exception("La clave es mas grande que el texto")
    except:
        y= []
        x= np.random.randint(1, len(string))
        for _ in range(x):
            y.append(np.random.randint(26))
        key = g.numtochar(y)
        return key

def cipherText(string, key):
    cipher_text = []
    string = g.chartonum(string)
    key = g.chartonum(key)
    for i in range(len(string)):
        x = (string[i] + key[i%len(key)]) % 26
        cipher_text.append(x)
    return "".join(g.numtochar(cipher_text).upper())


def DecryptedText(cipher_text, key):
    orig_text = []
    cipher_text = g.chartonum(cipher_text)
    key = g.chartonum(key)
    for i in range(len(cipher_text)):
        x = (cipher_text[i] - key[i%len(key)] + 26) % 26
        orig_text.append(x)
    return ("".join(g.numtochar(orig_text))).upper()


if __name__ == "__main__":
    string = str(input())
    keyword = str(input())
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Ciphertext :", cipher_text)
    ciphertext = str(input())
    print("Original/Decrypted Text :",
          DecryptedText(ciphertext, key))
