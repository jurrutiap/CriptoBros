import utils.globals as g
import os

def ShiftCipherCryptanalysis(text):
    f= open("utils/results.txt", "w")
    clearText = ''.join(ch for ch in text if ch.isalpha())
    textAsNumber = g.chartonum(clearText)
    f.write(f'SHIFT CRIPTO ANALYSIS\n\nCIPHER TEXT: {text}\n-------------------------------------------------\n\n')
    for des in range(26):
        displacedText = [(char - des)%26 for char in textAsNumber]
        posibleText = g.numtochar(displacedText)
        f.write(f"With key {des}, the clear text is {posibleText} \n")
    f.close()

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    decriptedTexts =ShiftCipherCryptanalysis(message)
    f= open("criptosite/utils/text.txt", "r")
    print(f.read())
    f.close()



