import globals as g

def ShiftCipherCryptanalysis(text):
    PossibleTexts = []
    clearText = ''.join(ch for ch in text if ch.isalpha())
    textAsNumber = g.chartonum(clearText)
    for des in range(26):
        displacedText = [(char - des)%26 for char in textAsNumber]
        posibleText = g.numtochar(displacedText)
        PossibleTexts.append(f"Assuming the key is {des}, the text is \n {posibleText}")
    return PossibleTexts

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    decriptedTexts =ShiftCipherCryptanalysis(message)
    for posib in decriptedTexts:
        print(posib)



