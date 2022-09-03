import math as m
import numpy as np

# Función principal
def main():
    message = input('Introducir Mensaje: ').lower()
    key = k(message)
    cifrado = cifrarMensaje(key, message)
    print('cifrado:\n%s' %(cifrado))
    print("\n")
    descifrado = descifrarMensaje(key, cifrado)
    print('descifrado:\n%s' %(descifrado))
    print("\n")

def k(text):
    control= True
    while control:
        try:
            K= int(input('Introducir Key [2-%s]: ' % (len(text) - 1)))
            if (K>2 and K<(len(text)-1)):
                print(K)
                control = False
            else:
                pass
        except:
            K= np.random.randint(2,(len(text) - 1))
            print("Se eligio una clave random")
            print(K)
            control = False
    return K

def cifrarMensaje(key, message):

    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

def descifrarMensaje(key, message):

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

    return "".join(plainText)

if __name__ == '__main__':
    main()