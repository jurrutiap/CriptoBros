# Implementation of Affine Cipher in Python
import globals as g
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
    return ''.join([chr(((key[0] * (t) + key[1]) % 26)
                        + ord('A')) for t in text])


# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
    '''
	P = (a^-1 * (C - b)) % 26
	'''
    cipher=g.chartonum(cipher)
    return ''.join([chr(((modinv(key[0], 26) * (c - key[1]))
                         % 26) + ord('A')) for c in cipher])


# Driver Code to test the above functions
def main():
    # declaring text and key
    text = str(input("message"))#'AFFINE CIPHER'
    key = list(map(int, str(input("key")).split())) #17,20

    # calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format(affine_encrypted_text))

    # calling decryption function
    print('Decrypted Text: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))


if __name__ == '__main__':
    main()
