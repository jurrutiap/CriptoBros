import globals as g


def generateKey(string, key):
    key = list(key)
    if len(string) > len(key):
        if len(string) == len(key):
            return (key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)
    else:
        quit()

def cipherText(string, key):
    cipher_text = []
    string = g.chartonum(string)
    key = g.chartonum(key)
    for i in range(len(string)):
        x = (string[i] + key[i]) % 26
        cipher_text.append(x)
    return "".join(g.numtochar(cipher_text).upper())


def DecryptedText(cipher_text, key):
    orig_text = []
    cipher_text = g.chartonum(cipher_text)
    key = g.chartonum(key)
    for i in range(len(cipher_text)):
        x = (cipher_text[i] - key[i] + 26) % 26
        orig_text.append(x)
    return ("".join(g.numtochar(orig_text)))


if __name__ == "__main__":
    string = str(input())
    keyword = str(input())
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Ciphertext :", cipher_text)
    ciphertext = str(input())
    print("Original/Decrypted Text :",
          DecryptedText(ciphertext, key))
