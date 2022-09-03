from pydoc import plain
import numpy as np
import globals as g


def encrypt(P, K):
    cipherMatrix = [0 for i in range(len(K))]
    for j in range(len(K)):
        for x in range(len(K)):
            cipherMatrix[j] += (K[x][j] *
                                P[x])
        cipherMatrix[j] = cipherMatrix[j] % 26
    return cipherMatrix

def dencrypt(cipher_text, K):
    K_inv = MatrixInverse(K)            
    plain_text = Hill(cipher_text, K_inv)
    return plain_text

def Hill(message, K):
    text = []
    message = g.chartonum(message)
    # Transform the message 3 characters at a time
    for i in range(0, len(message), len(K)):
        P = [0 for i in range(len(K))]
        # Assign the corresponfing integer value to each letter
        for j in range(len(K)):
            P[j] = message[i + j]
        # Encript three letters
        C = encrypt(P, K)
        # Add the encripted 3 letters to the final cipher text
        for j in range(len(K)):
            text.append(chr(C[j] + 65))
        # Repeat until all sets of three letters are processed.

    # return a string
    return "".join(text)


def MatrixInverse(K):
    det = int(np.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = np.delete(Dji, (j), axis=0)
            Dji = np.delete(Dji, (i), axis=1)
            det = Dji[0][0] * Dji[1][1] - Dji[0][1] * Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1, i + j) * det) % 26
    return K_inv


def create_matrix_from(key):
    key = g.chartonum(key)
    if len(key) % 4 == 0:
        n = 4
    else:
        n = 3
    m = [[0] * 3 for i in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = key[n * i + j]
    return m

def k():
    control= True
    while control:
        try:
            K= str(input('Introducir Key:'))
            if K == "":
                raise Exception("Vacio")
            try:
                if(len(K)%3 == 0 or len(K)%4 == 0):
                    print(K)
                    control = False
            except:
                pass
        except:
            L=[]
            r= np.random.randint(1)
            if r == 0:
                for _ in range(9):
                    L.append(np.random.randint(26))
            elif r == 1:
                for _ in range(16):
                    L.append(np.random.randint(26))
            K= g.numtochar(L)
            print("Se eligio una clave random")
            print(K)
            control = False
    return K

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    key = k()  # "RRFVSVCCT"
    # Create the matrix K that will be used as the key
    K = create_matrix_from(key)
    # C = P * K mod 26
    cipher_text = Hill(message, K)
    print('Cipher text: ', cipher_text)
    decipher_text = dencrypt(cipher_text, K)
    print('Decipher text: ', decipher_text)
