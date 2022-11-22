import numpy as np
import imageio
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


def K(k):
    if len(k) == 24:
        return k
    else:
        return "ABCDEFGHIJKLMNOPQRSTUVXY"

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
    if len(h)%6 != 0:
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
    imageio.imwrite("criptosite/static/img/"+name, img)


def EncryptECB(key):
    """
    Function to encrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/clean.png')


    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"

    cipher = DES3.new(key.encode(),DES3.MODE_ECB)

    #padding
    if len(data)%cipher.block_size != 0:
        data +=  b"f" * (cipher.block_size - len(data)%cipher.block_size)

    d = cipher.encrypt(data)

    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Encrypted.png')






def DecryptECB(key):
    """
    Function to decrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/Encrypted.png')
    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"
    cipher = DES3.new(key.encode(), DES3.MODE_ECB)

    #padding
    if len(data)%cipher.block_size != 0:
        data +=  b"f" * (cipher.block_size - len(data)%cipher.block_size)

    d = cipher.decrypt(data)


    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Decrypted.png')



def EncryptCBC(key):
    """
    Function to encrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/clean.png')



    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"

    cipher = DES3.new(key.encode(),DES3.MODE_CBC, iv= iv)

    #padding
    if len(data)%cipher.block_size != 0:
        data +=  b"f" * (cipher.block_size - len(data)%cipher.block_size)

    d = cipher.encrypt(data)

    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Encrypted.png')







def DecryptCBC(key):
    """
    Function to decrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/Encrypted.png')


    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"
    cipher = DES3.new(key.encode(), DES3.MODE_CBC, iv = iv)

    #padding
    if len(data)%cipher.block_size != 0:
        data +=  b"f" * (cipher.block_size - len(data)%cipher.block_size)

    d = cipher.decrypt(data)


    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Decrypted.png')



def EncryptCFB(key):
    """
    Function to encrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/clean.png')



    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"

    cipher = DES3.new(key.encode(),DES3.MODE_CFB, iv= iv)


    d = cipher.encrypt(data)

    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Encrypted.png')




def DecryptCFB(key):
    """
    Function to decrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/Encrypted.png')


    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"
    cipher = DES3.new(key.encode(), DES3.MODE_CFB, iv = iv)


    d = cipher.decrypt(data)


    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Decrypted.png')



def EncryptOFB(key):
    """
    Function to encrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/clean.png')



    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"

    cipher = DES3.new(key.encode(),DES3.MODE_OFB, iv= iv)


    d = cipher.encrypt(data)

    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Encrypted.png')







def DecryptOFB(key):
    """
    Function to decrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/Encrypted.png')


    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"
    cipher = DES3.new(key.encode(), DES3.MODE_OFB, iv = iv)


    d = cipher.decrypt(data)


    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Decrypted.png')


def EncryptCTR(key):
    """
    Function to encrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/clean.png')


    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"

    cipher = DES3.new(key.encode(),DES3.MODE_CTR,nonce=iv[:len(iv)//2])

    #padding
    if len(data)%cipher.block_size != 0:
        data +=  b"f" * (cipher.block_size - len(data)%cipher.block_size)

    d = cipher.encrypt(data)

    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Encrypted.png')







def DecryptCTR(key):
    """
    Function to decrypt
    imageToEncrypt: a string, representing the direction of the image
    key: a key. MUST be an 8 byte long bytes object
    """

    dataToEncrypt = ImageToBytes('criptosite/static/img/Encrypted.png')


    data = dataToEncrypt[0]


    originalRows, originalColumns = dataToEncrypt[1][0],dataToEncrypt[1][1]

    iv = b"00000000"
    cipher = DES3.new(key.encode(), DES3.MODE_CTR,nonce=iv[:len(iv)//2])

    #padding
    if len(data)%cipher.block_size != 0:
        data +=  b"f" * (cipher.block_size - len(data)%cipher.block_size)

    d = cipher.decrypt(data)


    BytesToImage(d,originalRows,originalColumns,'criptosite/static/img/Decrypted.png')





