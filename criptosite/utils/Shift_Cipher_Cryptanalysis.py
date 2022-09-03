import globals as g

def ShiftCipherCryptanalysis(text):
    clearText = ''.join(ch for ch in text if ch.isalpha())
    textAsNumber = g.chartonum(clearText)
    for des in range(26):
        displacedText = [(char - des)%26 for char in textAsNumber]
        posibleText = g.numtochar(displacedText)
        print(f"Assuming the key is {des}, the text is \n {posibleText}")



if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    ShiftCipherCryptanalysis(message)



