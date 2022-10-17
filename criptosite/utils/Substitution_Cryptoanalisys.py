
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def SubstitutionCryptoanalisys(text):
    f= open("utils/results.txt", "w")
    f.write(f'SUBSTITUTION CRIPTO ANALYSIS\n\nCLEAR TEXT: {text}\n-------------------------------------------------\n\n')
    clearText = ''.join(ch for ch in text if ch.isalpha())
    frecuenciesLetters = {}
    frecuenciesBigrams = {}
    for letter in ALPHABET:
        frecuenciesLetters[letter] = clearText.count(letter)
        f.write(f' LETTER: {letter} FRECUENCE: {frecuenciesLetters[letter]}\n')
    print(frecuenciesLetters)

    for letterOne in ALPHABET:
        for letterTwo in ALPHABET:
            count = clearText.count(letterOne+letterTwo)
            if count == 0:
                continue
            frecuenciesBigrams[letterOne+letterTwo] = count
            f.write(f'LETTER: {letterOne+letterTwo} FRECUENCE: {frecuenciesBigrams[letterOne+letterTwo]} \n')
    print(frecuenciesBigrams)

    f.close()

#message = """LIVITCSWPIYVEWHEVSRIQMXLEYVEOIEWHRXEXIPFEMVEWHKVSTYLXZIXLIKIIXPIJVSZEYPERRGERIM
#WQLMGLMXQERIWGPSRIHMXQEREKIETXMJTPRGEVEKEITREWHEXXLEXXMZITWAWSQWXSWEXTVEPMRXRSJ
#GSTVRIEYVIEXCVMUIMWERGMIWXMJMGCSMWXSJOMIQXLIVIQIVIXQSVSTWHKPEGARCSXRWIEVSWIIBXV
#IZMXFSJXLIKEGAEWHEPSWYSWIWIEVXLISXLIVXLIRGEPIRQIVIIBGIIHMWYPFLEVHEWHYPSRRFQMXLE
#PPXLIECCIEVEWGISJKTVWMRLIHYSPHXLIQIMYLXSJXLIMWRIGXQEROIVFVIZEVAEKPIEWHXEAMWYEPP
#XLMWYRMWXSGSWRMHIVEXMSWMGSTPHLEVHPFKPEZINTCMXIVJSVLMRSCMWMSWVIRCIGXMWYMX"""

if __name__ == "__main__":
    message = str(input("Message:"))
    decriptedTexts =SubstitutionCryptoanalisys(message)


