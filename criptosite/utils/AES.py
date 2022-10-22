from Crypto.Cipher import AES
from PIL import Image
import requests
from PIL import ImageOps
import urllib.request
import numpy as np
import codecs
from secrets import token_bytes

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

# ECB
def encode_aes_img_ECB(key, url):
	cipher = AES.new(key, AES.MODE_ECB)
	img = Image.open("criptosite/static/img/AES/AES_image.jpg")
	encryptedImg = img.convert("RGBA")

	# Resize image as needed, the image width must be a multiple
	# of 4
	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	
	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	
	# Show the image and save it in a .pgm file
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/AES/EncryptedImgAES.png")

def decode_aes_img_ECB(key, url):
	cipher = AES.new(key, AES.MODE_ECB)
	img = Image.open(url)
	decryptedImg = img

	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	decryptedImg.save("criptosite/static/img/AES/DecryptedImgAES.png")

#CBC
def encode_aes_img_CBC(key, url, iv=None):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	img = Image.open("criptosite/static/img/AES/AES_image.jpg")
	encryptedImg = img.convert("RGBA")

	# Resize image as needed, the image width must be a multiple
	# of 4
	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	
	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	
	# Show the image and save it in a .pgm file
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/AES/EncryptedImgAES.png")
	return (cipher.iv).hex()

def decode_aes_img_CBC(key, url, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	img = Image.open(url)
	decryptedImg = img

	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	decryptedImg.save("criptosite/static/img/AES/DecryptedImgAES.png")

#OFB
def encode_aes_img_OFB(key, url, iv=None):
	cipher = AES.new(key, AES.MODE_OFB, iv)
	img = Image.open("criptosite/static/img/AES/AES_image.jpg")
	encryptedImg = img.convert("RGBA")

	# Resize image as needed, the image width must be a multiple
	# of 4
	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	
	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	
	# Show the image and save it in a .pgm file
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/AES/EncryptedImgAESOFB.png")
	return (cipher.iv).hex()

def decode_aes_img_OFB(key, url, iv):
	cipher = AES.new(key, AES.MODE_OFB, iv)
	img = Image.open(url)
	decryptedImg = img

	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	decryptedImg.save("criptosite/static/img/AES/DecryptedImgAESOFB.png")

#CFB
def encode_aes_img_CFB(key, url, iv=None):
	cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
	img = Image.open("criptosite/static/img/AES/AES_image.jpg")
	encryptedImg = img.convert("RGBA")

	# Resize image as needed, the image width must be a multiple
	# of 4
	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	
	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	
	# Show the image and save it in a .pgm file
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/AES/EncryptedImgAES.png")
	return (cipher.iv).hex()

def decode_aes_img_CFB(key, url, iv):
	cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
	img = Image.open(url)
	decryptedImg = img

	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	decryptedImg.save("criptosite/static/img/AES/DecryptedImgAES.png")

#CTR
def encode_aes_img_CTR(key, url, nonce=None):
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	img = Image.open("criptosite/static/img/AES/AES_image.jpg")
	encryptedImg = img.convert("RGBA")

	# Resize image as needed, the image width must be a multiple
	# of 4
	if encryptedImg.width % 4 != 0:
		diff = 4 - (encryptedImg.width % 4)
		encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
	
	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	
	# Show the image and save it in a .pgm file
	#encryptedImg.show()
	encryptedImg.save("criptosite/static/img/AES/EncryptedImgAES.png")
	return (cipher.nonce).hex()

def decode_aes_image_ctr(key, url, nonce):
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	img = Image.open(url)
	decryptedImg = img

	# Iterate over each row of the image height taking at each step
	# 4 pixels to transform them into a new 4 pixels
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
	decryptedImg.save("criptosite/static/img/AES/DecryptedImgAES.png")


key = "7EAB923792032CBA5F6046022B963826"
bin_key = codecs.decode(key, 'hex_codec')
print(bin_key)
#iv = encode_aes_image_ofb(bin_key, "https://upload.wikimedia.org/wikipedia/commons/5/56/Tux.jpg?20090323211402")
#decode_aes_image_ofb(bin_key, "result.png", codecs.decode(iv, 'hex_codec'))