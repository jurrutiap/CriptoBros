import string
ALFABET = string.ascii_uppercase

USUALFREQUENCIES = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.024, 0.002, 0.02, 0.001]

def VigenereCryptoanalisys(possibleKeyLen, text):
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

        possibleKey.append(frequencies.index(likelyKeyElement))

    possibleKey = ''.join(ALFABET[x] for x in possibleKey)
    answer = f"if the key lenght is {possibleKeyLen}, the key is {possibleKey}"

    return answer

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


print(VigenereCryptoanalisys(5,message))
