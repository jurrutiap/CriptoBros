from Crypto.Cipher import DES
from Crypto.Hash import SHA256
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
import imageio
import numpy as np

salt_const = b"$ez*}-d3](%d%$#*!)$#%s45le$*fhucdivyanshu75456dgfdrrrrfgfs^"
pi = 100005


def K(k):
    if (len(k) == 8):
        return k
    else:
        return "ABCDEFGH"

def rgb2hex(rgb):

    """
    convert a list or tuple of RGB values
    to a string in hex
    """

    r,g,b = rgb
    return '{:02x}{:02x}{:02x}'.format(r, g, b)


def arrayToString(array):
    """
    convert an array to a string
    """

    string = ""
    for element in array:
        string += str(element)

    return string


def sliceStr(string,sliceLenght):
    """
    slice a string in chunks of sliceLenght lenght
    """

    string = str(string)
    array = np.array([string[i:i+sliceLenght] for i in range(0,len(string),sliceLenght)])
    return array



def hexToRGB(hexadecimal):
    """
    convert a hex string to an array of RGB values
    """
    h = hexadecimal.lstrip('#')
    if len(h)!=6:
        return
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]

def ImageToBytes(image):
    image = imageio.imread(image)
    # Drop the alpha channel.
    if image.shape[2] == 4:
        image = image[..., :3]
    # Convert to bytes directly.

    originalRows, originalColumns,_ = image.shape
    byteImage = image.tobytes()
    return (byteImage, [originalRows,originalColumns])

def BytesToImage(byteToConvert, originalRows, originalColumns, name):

    size = originalRows * originalColumns * 3

    if size < len(byteToConvert):
        usefulLenght = len(byteToConvert)% size
        byteToConvert = byteToConvert[:-1*usefulLenght]

    elif size > len(byteToConvert):
        usefulLenght = size - len(byteToConvert)
        byteToConvert += bytes.fromhex("ff") * usefulLenght

    img = np.frombuffer(byteToConvert, np.uint8).reshape(originalRows, originalColumns, 3)
    imageio.imwrite("criptosite/static/img/"+name,img)


def encryptDESImage(key):
    # opening the image file
    image = ImageToBytes('criptosite/static/img/clean.png')

    oriRows = image[1][0]
    oriCols = image[1][1]
    image = image[0]

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
    BytesToImage(ciphertext1,oriRows,oriCols,"Encrypted.png")
    return key


def decryptDESImage(key):
    # opening the image file
    image = ImageToBytes('criptosite/static/img/Encrypted.png')

    oriRows = image[1][0]
    oriCols = image[1][1]
    encrypted_data_with_hash = image[0]

    key_dec = key

    # extracting hash and cipher data without hash
    extracted_hash = encrypted_data_with_hash[-32:]
    encrypted_data = encrypted_data_with_hash[:-32]

    # salting and hashing password
    key_dec = PBKDF2(key_dec, salt_const, 48, count=pi)


    # padding
    while len(encrypted_data) % 8 != 0:
        encrypted_data += b" "

    # decrypting using triple 3 key DES
    cipher1 = DES.new(key_dec[0:8], DES.MODE_CBC, key_dec[24:32])
    plaintext1 = cipher1.decrypt(encrypted_data)

    # hashing decrypted plain text
    hash_of_decrypted = SHA256.new(data=plaintext1)

    # saving the decrypted file

    BytesToImage(plaintext1,oriRows,oriCols,"Decrypted.png")
    return key


