from Cryptodome.Cipher import DES
from Cryptodome.Hash import SHA256
from getpass import getpass
from Cryptodome.Protocol.KDF import PBKDF2

salt_const = b"$ez*}-d3](%d%$#*!)$#%s45le$*fhucdivyanshu75456dgfdrrrrfgfs^"
pi = 100005


def encryptDESImage(key):
    # opening the image file

    with open('criptosite/static/img/clean.png', 'rb') as imagefile:
        image = imagefile.read()

    # padding
    while len(image) % 8 != 0:
        image += b" "

    # hashing original image in SHA256
    hash_of_original = SHA256.new(data=image)
    key_enc = PBKDF2(key, salt_const, 48, count=pi)

    # Encrypting using triple 3 key DES

    cipher1 = DES.new(key_enc[0:8], DES.MODE_CBC, key_enc[24:32])
    ciphertext1 = cipher1.encrypt(image)

    # Adding hash at end of encrypted bytes
    ciphertext1 += hash_of_original.digest()

    # Saving the file encrypted
    with open('criptosite/static/img/Encrypted.png', 'wb') as image_file:
        image_file.write(ciphertext1)
    return key


def decryptDESImage(key):
    with open('criptosite/static/img/Encrypted.png', 'rb') as encrypted_file:
        encrypted_data_with_hash = encrypted_file.read()

    key_dec = key

    # extracting hash and cipher data without hash
    extracted_hash = encrypted_data_with_hash[-32:]
    encrypted_data = encrypted_data_with_hash[:-32]

    # salting and hashing password
    key_dec = PBKDF2(key_dec, salt_const, 48, count=pi)

    # decrypting using triple 3 key DES
    cipher1 = DES.new(key_dec[0:8], DES.MODE_CBC, key_dec[24:32])
    plaintext1 = cipher1.decrypt(encrypted_data)

    # hashing decrypted plain text
    hash_of_decrypted = SHA256.new(data=plaintext1)

    # saving the decrypted file
    with open('criptosite/static/img/Decrypted.png', 'wb') as image_file:
        image_file.write(plaintext1)
    return key


def finalDESImage(file_name, key):
    encryptDESImage(file_name, key)
    decryptDESImage(file_name, key)

# a = encryptDESImage('lena.jpg', 'aBcdefghfegrds54')
# print(a)
# b = decryptDESImage('lena.jpg', 'aBcdefghfegrds54')
