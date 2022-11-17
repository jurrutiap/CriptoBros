from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Util.number import ceil_div, bytes_to_long, long_to_bytes

public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoVlefpIw0RYMWdIn0jCk
S2xy3EQnN+kJELcDfZWw0pNHDUwbRW9fl0iGabNn1ZLz4akbhtqA24ErwzdmqzSi
fxTgfuWLGYxbp7Tzs0vmz61F6xSnPZhwE/XyboC+E9M0Kyr4Pp68E51hVBpz/jj4
FVgMMWo3y1uSzAqDquHSy6c4fGs17ekBxcVSK0GqKEr3nkhcW3w/zZRluXttTpWF
MLAAjD2AQvPtHzLB+V6gsqIAn2cxC+ie8CrA/WD7TZ8lqM3dps5mye3wyT12ywf+
8qf/eQ8oUNWqalPYXeBIIMfsUSUMql1i14DED3LDBa+rtsC0BWyTI3w/dV3Q6gvx
HQIDAQAB
-----END PUBLIC KEY-----"""

private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAoVlefpIw0RYMWdIn0jCkS2xy3EQnN+kJELcDfZWw0pNHDUwb
RW9fl0iGabNn1ZLz4akbhtqA24ErwzdmqzSifxTgfuWLGYxbp7Tzs0vmz61F6xSn
PZhwE/XyboC+E9M0Kyr4Pp68E51hVBpz/jj4FVgMMWo3y1uSzAqDquHSy6c4fGs1
7ekBxcVSK0GqKEr3nkhcW3w/zZRluXttTpWFMLAAjD2AQvPtHzLB+V6gsqIAn2cx
C+ie8CrA/WD7TZ8lqM3dps5mye3wyT12ywf+8qf/eQ8oUNWqalPYXeBIIMfsUSUM
ql1i14DED3LDBa+rtsC0BWyTI3w/dV3Q6gvxHQIDAQABAoIBABAk7pEQlKTfJWY5
YnWkG1RWqhmDEj+EaD1NaqJ+v14akXHxqwrkDXcIMTbTVjDnDtMGBjSUmW8dOiFC
4lmAH0BC+QGJe0UXp7Yco4PNtO8Twdq3StKddZ1xrwvCgwJd0Cr/li5B2MTHqwzs
xq1pytzr3fB11dZZt9MFvE31YY+x54bGDaMYRvSSy0sHSreIEJiHoBAt6s7onB0/
LNltOFiMegnOjbN5wy2LByY5JrHgtUHxaaAsnI7pXKDSYOLLvZiaTKMl7Atltmkv
s80MoLgCn9oN/k1+WTZW8vVfdBpEHLjd2NJpFY/V6g2jHnfczIHacOvt1O2SrBvO
J56pPvECgYEAyMFMHJlVX1fAOD6c9/aImnYlxANYt1Fj9J1S+1FrMZy+RA/Sh87U
iNm+0uOeQWTOFNrBUUtwWfQiBmX/45SxY+2lp5xHlw3v2QFj9luWFy4Wu91ZAq0y
74MczYVwUw5pqvfksPId4gg16hgJ9gB7OujSi9mkk2IgChi+7h0X8XUCgYEAzcAE
jkRH+XRBqAjEj+LAlSeodQV5UoomInOTO8JolV47sVlHZ8reip2OdB749oCBLAVZ
ULpj0sYzuqSJBY/zu+acoud3jyGkCWsMgcq4tky5Fuu6gWbJfPDF+RbsUV8can8x
4woO+nqO/7IloTMQyIoLBAaWIcghLIowT2VAJAkCgYEAsfPOMOemao5RYEn4QEDz
k9+42EiTImRuMw4l2Yqxd1fWvGQ+HY40jV5erXeA97yQhKHojNRPMh2a74sIycYr
fEXS+oEoYHjFK9n0rxM+NyvukPbDiQDYTsEtDe0DxUvYVOnKeSMVZCAdEnXeloaU
tYJd6AOzw8VOW0TWMiHt8GUCgYAroc7VhLFmuzq5MbLNeJ6ygsh8mH6T/Gv93liY
0a9wDZ3HDFHSNvlel+7/vRm63KGH/lJkhkJpDlMl/4J3RYHAlTUebsux9MZeoO70
D1OAhWCy9aaFjpCoCD9ThYLz9qGGDBc+OIHYqGju3I6SUsv6Wxve7K6l11UBpwR7
sdMaUQKBgGk7rNfmndbVx9AStoBIdfx8t/mOrTrKsHkwnsmM09OADp1pRqzjA5qb
pOfoxfk3icuKzrCgKVeH9drhLmy87KyQqppofAkZ9lHgUefX9cyOQ25JoWdXT4Lp
0hAQWo/B6VzSNOzq2vN00RfdEWJpgl7qfBn2QHEzSB5gAeoGJg+/
-----END RSA PRIVATE KEY-----"""

# bit_size = 2048
# key_format = 'PEM'
public_key = RSA.importKey(public_key_string)
private_key = RSA.importKey(private_key_string)


def RSAEncryption(plain_text):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_data = cipher_rsa.encrypt(plain_text.encode())
    enc_data = str(bytes_to_long(enc_data))
    return enc_data, private_key_string


def RSADecryption(plain_text):
    plain_text = long_to_bytes(int(plain_text))
    decipher_rsa = PKCS1_OAEP.new(private_key)
    dec_data = decipher_rsa.decrypt(plain_text)
    return dec_data.decode(), private_key_string

# def showPublicKey(keys):
#     return keys.publickey().export_key(key_format).decode()
#
#
# def showPrivateKey(keys):
#     return keys.export_key(key_format).decode()


# # encryption/decryption
# enc = RSAPreviousEncryption('Hola Mundo')
# print(enc[0])
# dec = RSAPreviousDecryption(enc[0])
# print(dec[0])
# # showing the keys
# print(showPublicKey(enc[1]))
# print(showPrivateKey(enc[1]))

# enc = RSAEncryption("Hellow World")
# print(enc)
# dec = RSADecryption(enc[0])
# print(dec)
