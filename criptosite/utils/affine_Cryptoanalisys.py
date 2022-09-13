INVERTIBLENUMBERS = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}
import utils.globals as g


## PARAMETERS
##  text: text to be analized

#The function will return the proper text
#If, and only if, the in (a,b) key used,
# a is invertible mod 26
def AffineCryptoanalisys(text):
    f= open("utils/results.txt", "w")
    f.write(f'AFFINE CRIPTO ANALYSIS\n\nCLEAR TEXT: {text}\n-------------------------------------------------\n\n')

    #clear the text of any non alphabet character
    clearText = ''.join(ch for ch in text if ch.isalpha())

    #convert the characters to numbers
    textAsNumber = g.chartonum(clearText)

    #for each a that is invertible mod 26
    for a in INVERTIBLENUMBERS:

        #for each b in integer mod 26
        for b in range(26):

            #calculate the original character for all characters in our
            #cipher text
            # by substracting b and multiplying by a
            displacedText = [(a * (char - b))%26 for char in textAsNumber]

            # convert the numbers to letters
            posibleText = g.numtochar(displacedText)

            # and add to the list of possible texts with
            # a message about the INVERSE[a] used (since a should be the multiplicative
            # inverse of the original a) and the b used
            f.write(f"Assuming the keys are {INVERTIBLENUMBERS[a]} and {b}, the text is {posibleText}\n")
    f.close()

if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    decriptedTexts =AffineCryptoanalisys(message)
    for posib in decriptedTexts:
        print(posib)


