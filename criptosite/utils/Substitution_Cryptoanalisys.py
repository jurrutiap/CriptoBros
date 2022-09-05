
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def SubstitutionCryptoanalisys(text):
    clearText = ''.join(ch for ch in text if ch.isalpha())
    frecuenciesLetters = {}
    frecuenciesBigrams = {}
    for letter in ALPHABET:
        frecuenciesLetters[letter] = clearText.count(letter)
    print(frecuenciesLetters)

    for letterOne in ALPHABET:
        for letterTwo in ALPHABET:
            count = clearText.count(letterOne+letterTwo)
            if count == 0:
                continue
            frecuenciesBigrams[letterOne+letterTwo] = count
    print(frecuenciesBigrams)

    return frecuenciesLetters,frecuenciesBigrams

#message = """LIVITCSWPIYVEWHEVSRIQMXLEYVEOIEWHRXEXIPFEMVEWHKVSTYLXZIXLIKIIXPIJVSZEYPERRGERIM
#WQLMGLMXQERIWGPSRIHMXQEREKIETXMJTPRGEVEKEITREWHEXXLEXXMZITWAWSQWXSWEXTVEPMRXRSJ
#GSTVRIEYVIEXCVMUIMWERGMIWXMJMGCSMWXSJOMIQXLIVIQIVIXQSVSTWHKPEGARCSXRWIEVSWIIBXV
#IZMXFSJXLIKEGAEWHEPSWYSWIWIEVXLISXLIVXLIRGEPIRQIVIIBGIIHMWYPFLEVHEWHYPSRRFQMXLE
#PPXLIECCIEVEWGISJKTVWMRLIHYSPHXLIQIMYLXSJXLIMWRIGXQEROIVFVIZEVAEKPIEWHXEAMWYEPP
#XLMWYRMWXSGSWRMHIVEXMSWMGSTPHLEVHPFKPEZINTCMXIVJSVLMRSCMWMSWVIRCIGXMWYMX"""

if __name__ == "__main__":
    message = str(input("Message:"))
    decriptedTexts =SubstitutionCryptoanalisys(message)


