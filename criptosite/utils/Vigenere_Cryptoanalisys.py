import string
import utils.vigenere_system as vs
ALFABET = string.ascii_uppercase

USUALFREQUENCIES = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.024, 0.002, 0.02, 0.001]

def k(k):
    try:
        K= int(k)
    except:
        K = 5
    return K

def preProcessText(text):
    text = text.replace(' ', '')
    text = text.lower()
    processedText = ""
    for c in text:
        if ord(c) >= 97 and ord(c) <= 97 + 25:
            processedText += c
    return processedText

def IsValidMatrix(m):
    if len(m) != len(m[0]):
        raise "The matrix is not square"

def CreateSubstrings(m, text):
    text = preProcessText(text)
    substrings = []
    for i in range(0, m):
        currSubstring = ""
        for j in range(i, len(text), m):
            currSubstring += text[j]
        substrings.append(currSubstring)
    return substrings

def GuessKeywordLength(k, text):
    lessDiff = 3
    guess = 0
    for m in range(1, k + 1):
        y_m = CreateSubstrings(m, text)
        IOCs = []
        for y in y_m:
            IOCs.append(GetIndexOfCoincidence(y))
        iocsAverage = sum(IOCs) / len(IOCs)
        diff = abs(0.065 - iocsAverage)
        if diff < lessDiff:
            lessDiff = diff
            guess = m
    return guess

def GetIndexOfCoincidence(text):
    n = len(text)
    IOC = 0
    frequencies = GetFrequencies(text)
    for c in frequencies:
        IOC += frequencies[c]*(frequencies[c] - 1)
    return IOC/(n*(n - 1))


def GenerateAlphabet():
    alphabet = {}
    for i in range(97, 97 + 26):
        alphabet[chr(i)] = 0
    return alphabet

def GetFrequencies(text):
    frequencies = GenerateAlphabet()
    for c in text:
        frequencies[c] += 1
    return frequencies


def VigenereCryptoanalisys(text):
    possibleKeyLen = GuessKeywordLength(15, text)
    f= open("utils/results.txt", "w")
    f.write(f'VIGENERE CRIPTO ANALYSIS\n\nENCRIPTED TEXT: {text}\nKEY LENGHT: {possibleKeyLen}\n-------------------------------------------------\n\n')
    #Clear text from non alphabet characters
    clearText = ''.join(ch.upper() for ch in text if ch.isalpha())

    #Dict to store the substrings
    wordsegments = {}

    ## These for separate the string in five lists
    ## stored in the dictionary
    ## so we divide the string in blocks of (at most) lenght possibleKeyLengt
    ## and each first character goes to list 1
    ## each second to list 2
    ## and so on

    #Go over the string in stepts of
    #possibleKeyLen lenght
    for i in range(0,len(clearText), possibleKeyLen):

        #for each of these substrings
        for j in range(possibleKeyLen):

            #if it's the first step
            #we create the dictionary entry
            if i== 0:
                #create the dictionary entry
                #ads the j-th character of the substring
                wordsegments[j] = clearText[j]

            #else, if we have characters to add
            #(so, if we haven't surpased the lenght of the string)
            #this is useful if we can't divide the string cleanly
            #into blocks of equal size
            elif j+i < len(clearText):

                #concatenate the j-th element of the substring i
                #to the string in the j-th index of the dictionary
                wordsegments[j] += clearText[j+i]


    #we calculate the lenght of (most) of the substrings
    nprime = len(clearText)//possibleKeyLen

    # A list to store the possible key
    possibleKey = []

    # For each list of characters
    for i in range(possibleKeyLen):

        #create a list to store the frequencies analyses
        frequencies = []

        #for each posible shift
        for g in range(26):

            total = 0

            # Do frequency analysis
            for j in range(26):
                freq = USUALFREQUENCIES[j] * wordsegments[i].count(ALFABET[(j+g)%26])/nprime
                total += freq
            frequencies.append(total)

        # Search the element that has the frequency
        # closest to the expected value
        likelyKeyElement = min(frequencies, key=lambda x:abs(x-0.065))
        f.write(f'FRECUENCE: {likelyKeyElement} LETTER: {frequencies.index(likelyKeyElement)}\n')

        possibleKey.append(frequencies.index(likelyKeyElement))

    possibleKey = ''.join(ALFABET[x] for x in possibleKey)
    f.write(f"\nIf the key lenght is {possibleKeyLen}, the key is '{possibleKey}'\n")

    clear_text = vs.DecryptedText(text, possibleKey)
    f.write(f'\nDECRIPTED TEXT: {clear_text}')

    f.close()
    print('done')

message = """nifon aicum niswt luvet vxshk nissx wsstb husle chsnv ytsro
cdsoy nisgx lnona chvch gnonw yndlh sfrnh npblr yowgf unoca
cossu ouoll iuvef issoe xgosa cpbew uormh lftaf cmwak bbbdv
cqvek muvil qbgnh ntiri ljgig atwnv yuvev iorim cpbsb hxviv
buvet vxshk uorim mjbdb pjrut fbueg ntgof yuwmx miodm ipdek
uuswx lfjek sewfy yssnm zscmm bpgeb huvez ysaag usaew mffvb
wfgim qpilw bbjeu yfbef vbfrt mtwnz uorig wpbvx hjsnm zpfag
uhsnm npglb jbqrh mttrh huwek mpfak ljjen hbbnh ooqew vzdak
udvum yucbx yoquf vffew vzonx hjumt lfgef vmwnz uxsiz bumag
xbbtb kvotx xumpx qswtx l"""

message2 = """CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBW
RVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIA
KLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJEL
XVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHR
ZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAM
RVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEW
EVKAKOEWADREMMXMTBHHCHRTKDNVRZCHRCLQOHPWQ
AIIWXNRMGWOIIFKEE
"""

message3 = """NOSEXTDUUNDZWCTSJTLXSVCPNDPQVEUUCLRKPJSNTBIEMIEOCPEDUWWOOC
PRAPFHEVGTLHOEUUDGSNVJVPCFCLPRPXACLFSFLRCVJTLPWPHBCSLPKTBSDPDNAUELOWETVM
DEAQRCIAWOEESAEGOTIVSPRSUTBSOZBGCBPFCIUSFMTYHGGFRPFHTITTTBIGLJBPCCUEECZY
GGQVAEDORIFNDPRCPPRELACUSIDTBHAVCTMIUMBGYLDGLMEYESUQVELNQWMTAYPFQSOENYWU
LVLECWEETCZYUWEBEYPOPNFCWTPGRPVTEOGNJSTOORICUDQSTMFNEFAGUJNXLITITMLFFKSR
UTDQQNEIXPBVUNDFTRWITRSZBEUTEWTHRUSUDWOEIOILQSTMFNEFAPITLQPIIIBTDTHCMFTN
COUOSNLCSGSUAFNHQRWOWFHRAUUWEFKCJEDPGVFFLTDGGMQECOWCMJDGLFKUTJFDHQEOIXPHNEP"""


VigenereCryptoanalisys(message3)
