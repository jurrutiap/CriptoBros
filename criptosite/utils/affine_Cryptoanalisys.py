INVERTIBLENUMBERS = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}
import utils.globals as g

def AffineCryptoanalisys(text):
    f= open("utils/results.txt", "w")
    f.write(f'AFFINE CRIPTO ANALYSIS\n\nCLEAR TEXT: {text}\n-------------------------------------------------\n\n')
    clearText = ''.join(ch for ch in text if ch.isalpha())
    textAsNumber = g.chartonum(clearText)
    for a in INVERTIBLENUMBERS:
        for b in range(26):
            displacedText = [(a * (char - b))%26 for char in textAsNumber]
            posibleText = g.numtochar(displacedText)
            f.write(f"Assuming the keys are {INVERTIBLENUMBERS[a]} and {b}, the text is {posibleText}\n")
    f.close()

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    decriptedTexts =AffineCryptoanalisys(message)
    for posib in decriptedTexts:
        print(posib)


