import numpy as np
import imageio
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


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
    """
    Image to convert from image to bytes
    """
    dataToEncrypt =imageio.imread(image)

    if dataToEncrypt.shape[2] ==4:
        dataToEncrypt = np.delete(dataToEncrypt,3,2)

    originalRows, originalColumns,_ = dataToEncrypt.shape


    #converting rgb to hex
    hexToEncrypt = np.apply_along_axis(rgb2hex, 2, dataToEncrypt)
    hexToEncrypt = np.apply_along_axis(arrayToString, 1, hexToEncrypt)
    hexToEncrypt = str(np.apply_along_axis(arrayToString, 0, hexToEncrypt))

    byteImage = bytes.fromhex(hexToEncrypt)

    return (byteImage, [originalRows,originalColumns])

def BytesToImage(byteToConvert,originalRows,originalColumns,name):

    """
    Convert from Bytes to Image
    """
    encryptedData = byteToConvert.hex()


    stepOne = sliceStr(encryptedData,originalColumns*6)

    stepTwo = []

    for i in stepOne:
        step = sliceStr(i,6)

        #Add lost pixels
        while len(step) != originalColumns:
            step = np.append(step,"ffffff")
        stepTwo.append(step)


    stepThree = []
    for i in stepTwo:
        d = []
        for j in i:
            d.append(hexToRGB(j))

        if len(stepThree) < originalRows:
            stepThree.append(d)

        encryptedImg = np.asarray(stepThree)


    imageio.imwrite(name,encryptedImg)


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





