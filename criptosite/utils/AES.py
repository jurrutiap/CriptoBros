from re import A
from Cryptodome.Cipher import AES
from PIL import Image
import requests
from PIL import ImageOps
import codecs
from secrets import token_bytes

# ECB
def encode_aes_img_ECB(key):
	cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
	img = Image.open("criptosite/static/img/clean.png")
	encryptedImg = img.convert("RGBA")

	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	for y in range(0, encryptedImg.height):
		rowPixels = []
		for x in range(0, encryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.encrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			rowPixels += encryptedImg.getpixel((x,y))
	
	# encryptedImg.show()
	encryptedImg.save("criptosite/static/img/Encrypted.png")

def decode_aes_img_ECB(key):
	cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
	img = Image.open("criptosite/static/img/Encrypted.png")
	decryptedImg = img

	for y in range(0, decryptedImg.height):
		rowPixels = []
		for x in range(0, decryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.decrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			
			rowPixels += decryptedImg.getpixel((x,y))
	
	#decryptedImg.show()
	decryptedImg.save("criptosite/static/img/Decrypted.png") 
#CBC
def encode_aes_img_CBC(key,iv):

	cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
	img = Image.open("criptosite/static/img/clean.png")
	encryptedImg = img.convert("RGBA")

	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	for y in range(0, encryptedImg.height):
		rowPixels = []
		for x in range(0, encryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.encrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			rowPixels += encryptedImg.getpixel((x,y))
	
	# encryptedImg.show()
	encryptedImg.save("criptosite/static/img/Encrypted.png")
	return (cipher.iv).hex()

def decode_aes_img_CBC(key,iv):
	
	cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
	img = Image.open("criptosite/static/img/Encrypted.png")
	decryptedImg = img

	for y in range(0, decryptedImg.height):
		rowPixels = []
		for x in range(0, decryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.decrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			
			rowPixels += decryptedImg.getpixel((x,y))
	
	#decryptedImg.show()
	decryptedImg.save("criptosite/static/img/Decrypted.png")

 #OFB
def encode_aes_img_OFB(key,iv):
	cipher = AES.new(key.encode("utf8"), AES.MODE_OFB, iv.encode("utf8"))
	img = Image.open("criptosite/static/img/clean.png")
	encryptedImg = img.convert("RGBA")

	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	for y in range(0, encryptedImg.height):
		rowPixels = []
		for x in range(0, encryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.encrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			rowPixels += encryptedImg.getpixel((x,y))
	
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/Encrypted.png")
	return (cipher.iv).hex()

def decode_aes_img_OFB(key,iv):
	cipher = AES.new(key.encode("utf8"), AES.MODE_OFB, iv.encode("utf8"))
	img = Image.open("criptosite/static/img/Encrypted.png")
	decryptedImg = img

	for y in range(0, decryptedImg.height):
		rowPixels = []
		for x in range(0, decryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.decrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			
			rowPixels += decryptedImg.getpixel((x,y))
	
	#decryptedImg.show()
	decryptedImg.save("criptosite/static/img/Decrypted.png")

#CFB
def encode_aes_img_CFB(key,iv):
	cipher = AES.new(key.encode("utf8"), AES.MODE_CFB, iv.encode("utf8"), segment_size=128)
	img = Image.open("criptosite/static/img/clean.png")
	encryptedImg = img.convert("RGBA")

	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	for y in range(0, encryptedImg.height):
		rowPixels = []
		for x in range(0, encryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.encrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			rowPixels += encryptedImg.getpixel((x,y))
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/Encrypted.png")
	return (cipher.iv).hex()

def decode_aes_img_CFB(key,iv):
	cipher = AES.new(key.encode("utf8"), AES.MODE_CFB, iv.encode("utf8"), segment_size=128)
	img = Image.open("criptosite/static/img/Encrypted.png")
	decryptedImg = img

	for y in range(0, decryptedImg.height):
		rowPixels = []
		for x in range(0, decryptedImg.width):
			if x % 4 == 0 and x > 0:
				# Transform the 4 pixels using AES cipher
				#print(hex(int.from_bytes(bytes(rowPixels), "big")))
				newRowPixels = cipher.decrypt(bytes(rowPixels))
				#print(hex(int.from_bytes(newRowPixels, "big")))
				newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
				for i in range(x - 4, x):
					decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
				rowPixels = []
			
			rowPixels += decryptedImg.getpixel((x,y))
	
	#decryptedImg.show()
	decryptedImg.save("criptosite/static/img/Decrypted.png")

#CTR
def encode_aes_img_CTR(key):
    iv2 = b"00000000"
    cipher = AES.new(key.encode("utf8"),AES.MODE_CTR,nonce=iv2[:len(iv)//2])
    img = Image.open("criptosite/static/img/clean.png")
    encryptedImg = img.convert("RGBA")   

	# Resize image as needed, the image width must be a multiple
	# of 4
    if encryptedImg.width % 4 != 0:
        diff=4-(encryptedImg.width %4)
        encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
    for y in range(0, encryptedImg.height):
        rowPixels = []
        for x in range(0, encryptedImg.width):
            if x % 4 == 0 and x > 0:
                newRowPixels = cipher.encrypt(bytes(rowPixels))
                newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
                for i in range(x - 4, x):
                    encryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
                rowPixels = []
            rowPixels += encryptedImg.getpixel((x,y))
	
	# Show the image and save it in a .pgm file
    #encryptedImg.show()
    encryptedImg.save("criptosite/static/img/Encrypted.png")

def decode_aes_img_CTR(key):
    iv2 = b"00000000"
    cipher = AES.new(key.encode("utf8"),AES.MODE_CTR,nonce=iv2[:len(iv)//2])
    img = Image.open("criptosite/static/img/Encrypted.png")
    decryptedImg = img

	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
    for y in range(0, decryptedImg.height):
        rowPixels = []
        for x in range(0, decryptedImg.width):
            if x % 4 == 0 and x > 0:
                newRowPixels = cipher.encrypt(bytes(rowPixels))
                newRowPixels = HexToDecimal(hex(int.from_bytes(newRowPixels, "big"))[2:])
                for i in range(x - 4, x):
                    decryptedImg.putpixel((i,y), newRowPixels[i - (x-4)])
                rowPixels = []
            rowPixels += decryptedImg.getpixel((x,y))

    #decryptedImg.show()
    decryptedImg.save("criptosite/static/img/Decrypted.png")

def DecimalToHex(l):
	result = ""
	for i in l:
		if len(hex(i).split('x')[-1]) != 1:
			result += hex(i).split('x')[-1]
		else:
			result += '0' + hex(i).split('x')[-1]
	return result.upper()

def HexToDecimal(s):
	result = []
	while len(s) != 32:
		s = '0' + s
	for i in range(0, 32, 8):
		pixel = []
		for j in range(i, i+8, 2):
			pixel.append(int(s[j]+s[j+1], base=16))
		result.append(tuple(pixel))
	return result


key = "7EAB923792032CBA5F6046022B963826"
iv = "A"*16