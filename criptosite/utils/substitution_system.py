# Python program to demonstrate
# Substitution Cipher
import string
import numpy as np

"""
create a dictionary to store the substitution
for the given alphabet in the cipher
text based on the key
"""

def k(k):
    try:
        K= int(k)
    except:
        K= np.random.randint(100000000)
    return K

def cipher_text(plain_txt,key):
    dict1 = {}
    cipher_txt = []
    all_letters = string.ascii_letters
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]
    for char in plain_txt:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)

    return "".join(cipher_txt).upper()


"""
create a dictionary to store the substitution
for the given alphabet in the plain text
based on the key
"""

def DecryptedText(ciphertext, key):
    dict2 = {}
    all_letters = string.ascii_letters
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i - key) % (len(all_letters))]
    # loop to recover plain text
    decrypt_txt = []
    for char in ciphertext:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)

    return "".join(decrypt_txt).upper()


if __name__ == "__main__":
    plain_txt = str(input("message:"))  # "I am studying Data Encryption"
    key = int(input("Key:"))  # 4
    ciphertext = cipher_text(plain_txt,key)
    print("Ciphertext :", ciphertext)
    print("Recovered plain text :", DecryptedText(ciphertext,key))
