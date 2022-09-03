def chartonum (text):
    numlist=[]
    y= ''.join(ch for ch in text if ch.isalpha()).lower()
    x = list(y)
    for i in x:
        numlist.append(abs(ord(i)-97))
    return numlist

def numtochar(text):
    charlist=""
    for i in text:
        charlist+= chr(i+97)
    return charlist.upper()