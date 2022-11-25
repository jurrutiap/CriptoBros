from Crypto.Cipher import AES
import os
import binascii
import x25519



def encrypt_AES_GCM(msg, secretKey):
    iv = b"0"*16
    aesCipher = AES.new(secretKey, AES.MODE_CFB, iv = iv)
    ciphertext = aesCipher.encrypt(msg)
    return ciphertext

def decrypt_AES_GCM(ciphertext, secretKey):
    iv = b"0"*16
    aesCipher = AES.new(secretKey, AES.MODE_CFB,iv = iv)
    plaintext = aesCipher.decrypt(ciphertext)
    return plaintext


def encrypt_ECC(msg, privKey, pubKey):
    sharedECCKey = x25519.scalar_mult(privKey, pubKey)
    ciphertext = encrypt_AES_GCM(msg, sharedECCKey)
    return ciphertext.hex()

def decrypt_ECC(encryptedMsg, pubKey, privKey):
    sharedECCKey = x25519.scalar_mult(privKey, pubKey)
    plaintext = decrypt_AES_GCM(bytes.fromhex(encryptedMsg), sharedECCKey)
    return plaintext

def get_priv_key():
    return os.urandom(32)
def get_pub_key():
    return os.urandom(32)


msg = bytes('Hello there', 'utf-16')
print("original msg:", msg)
privKey = get_priv_key()
pubKey = x25519.scalar_base_mult(privKey)
sharedECCKey = x25519.scalar_mult(privKey, pubKey)
encryptedMsg = encrypt_ECC(msg, privKey, pubKey)
decryptedMsg = decrypt_ECC(encryptedMsg,pubKey,privKey)

print("decrypted msg:", decryptedMsg.decode("utf-16") )

