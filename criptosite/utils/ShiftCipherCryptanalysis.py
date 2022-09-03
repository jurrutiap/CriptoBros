ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def ShiftCipherCryptanalysis(text):
    textAsNumber = []
    clearText = ''.join(ch for ch in text if ch.isalpha())
    for char in clearText:
        pos= ALPHABET.index(char.upper())
        textAsNumber.append(pos)

    for des in range(26):
        posibleText = ""
        for char in textAsNumber:
            posibleText = posibleText + ALPHABET[(char - des)%26]
        print(f"Assuming the key is {des}, the text is \n {posibleText}")



if __name__ == "__main__":
    message = str(input("Message:"))  # "MYSECRETMESSAGE"
    ShiftCipherCryptanalysis(message)



