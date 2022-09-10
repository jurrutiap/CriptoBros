import math as m
import numpy as np

# Función principal

def k(k, text):
    try:
        if(int(k)>2 and int(k)<(len(text)-1)):
            K = int(k)
        else:
            raise Exception("K invalida")
    except:
        K= np.random.randint(2,(len(text) - 1))
    return K

def encrypt(key, message):

    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

def desencrypt(key, message):

    numCols = m.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0; row = 0;

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return "".join(plainText).upper()
