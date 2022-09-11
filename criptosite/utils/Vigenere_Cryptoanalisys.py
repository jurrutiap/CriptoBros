import string

ALFABET = string.ascii_uppercase

USUALFREQUENCIES = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.024, 0.002, 0.02, 0.001]

def VigenereCryptoanalisys(possibleKeyLen, text):
    clearText = ''.join(ch.upper() for ch in text if ch.isalpha())

    wordsegments = {}
    for i in range(0,len(clearText), possibleKeyLen):
        print(clearText[i:i+possibleKeyLen])
        for j in range(possibleKeyLen):
            if i== 0:
                wordsegments[j] = clearText[j]
            elif j+i < len(clearText):
                wordsegments[j] += clearText[j+i]

    nprime = len(clearText)//possibleKeyLen

    possibleKey = []
    for i in range(possibleKeyLen):
        frequencies = []
        for g in range(26):
            total = 0
            for j in range(26):
                freq = USUALFREQUENCIES[j] * wordsegments[i].count(ALFABET[(j+g)%26])/nprime
                total += freq
            frequencies.append(total)
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
