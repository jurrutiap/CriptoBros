INVERTIBLENUMBERS = [1,3,5,7,9,11,15,17,19,21,23,25]
import globals as g

def AffineCryptoanalisys(text):
    PossibleTexts = []
    clearText = ''.join(ch for ch in text if ch.isalpha())
    textAsNumber = g.chartonum(clearText)
    for a in INVERTIBLENUMBERS:
        for b in range(26):
            displacedText = [(a * (char - b))%26 for char in textAsNumber]
            posibleText = g.numtochar(displacedText)
            PossibleTexts.append(f"Assuming the keys are {a} and {b}, the text is {posibleText}")
    return PossibleTexts

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    decriptedTexts =AffineCryptoanalisys(message)
    for posib in decriptedTexts:
        print(posib)


