#recuperado de https://github.com/aman-17/rabin-cryptosystem
import random
from functools import reduce


def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
          199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
          317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
          443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
          577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
          701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
          839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
          983, 991, 997]
#


# n -> integer, return if n is prime or not
def isPrime(n):
    # Miller-Rabin Primality Test
    # 1. Factorize n - 1 as m * 2^k
    k = 0
    temp = n - 1
    while temp % 2 == 0:
        temp = temp // 2
        k += 1
    else:
        m = temp

    # 2. Primality Test
    # Test all entries in the 'primes' list
    for a in primes:
        x = [pow(a, m * (2 ** i), n) for i in range(0, k)]
        # If there is no -1 (n - 1) in the following blank, return 'composite'
        if pow(a, m, n) != 1 and none_in_x_is_n(x, n - 1):
            return False
        elif pow(a, m, n) == 1 or not none_in_x_is_n(x, n - 1):
            continue

    return True


# generate a 128-bit prime number
def generate_a_prime_number(num_of_bits):
    # keep creating a random 16-byte (128-bit) number until there is a prime number
    while 1:

        num = random.getrandbits(num_of_bits)
        if isPrime(num) and (num%4 == 3 or num%8== 5):
            return num
        else:
            continue


# Find SQROOT in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r


# Find SQROOT in Zp where p = 5 mod 8
def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p - 1) // 4, p)
    r =0
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8) % p

    return r




# Additional functions
def none_in_x_is_n(x, n):
    for i in x:
        if i == n:
            return False
    return True

#mark a solution
def padding(plaintext):
    binary_str = bin(plaintext)     # convert to a bit string
    output = binary_str + "00111111"     # add a mark
    return int(output, 2)       # convert back to integer

# encryption function

def encryption(plaintext, n,B):
    # c = m^2 mod n
    m = padding(plaintext)
    p = (m *(m+B))
    return p%n

def choose(lst):

    for i in lst:
        binary = bin(i)
        if "00111111" == binary[-8:]:
            return int(bin(i)[:-8],2)
    return "None"


# encryption function
def decryption(a, p, q, B):
    n = p * q
    r, s = 0, 0
    # find sqrt
    # for p
    addB = B/2


    y = int(((B**2)/4 % n) + a)
    if p % 4 == 3:
        r = sqrt_p_3_mod_4(y, p)
    elif p % 8 == 5:
        r = sqrt_p_5_mod_8(y, p)
    # for q
    if q % 4 == 3:
        s = sqrt_p_3_mod_4(y, q)
    elif q % 8 == 5:
        s = sqrt_p_5_mod_8(y, q)

    lst = [r, -1*r,s, -1*s]


    rest = [chinese_remainder([p,q],[a,b]) for a in (r, -1*r) for b in (s, -1*s)]

    posPlain = [int(i - addB) for i in rest]
    if choose(posPlain) != "None":
        return choose(posPlain)
    return posPlain


def delete_space(string):
    lst = string.split(' ')
    output = ''
    for i in lst:
        output += i
    return output


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


def RabinEncrypt(plaintext):
    #p = int(delete_space(input('p = ')), 32)   # p = daaefe652cad1614f17e87f2cd80973f
    #q = int(delete_space(input('q = ')), 32)   # q = f99988626723eef2a54ed484dfa735c7

    #p = 10000019
    #q = 55555333

    #p = 1666043
    #q = 2796203

    p = 10092003300140014003
    q = 36484957213536676883

    n = p*q


    B = int(delete_space("daae"), 32)
    if not 0 <= B < n:
        B = B%n

    upperbound = "01111010" + "00111111"
    sliceSize = -2
    while ((int(upperbound,2)**2) *(int(upperbound,2)+B)) < n:
        upperbound = "01111010" + upperbound
        sliceSize += 1

    if sliceSize >=1:
        ciphertext = []

        plaintextChunks = [plaintext[i:i+sliceSize] for i in range(0,len(plaintext),sliceSize)]
        for chunk in plaintextChunks:
            textToEncrypt = ""
            for char in chunk:
                textToEncrypt += format((ord(char)),"08b")
            textToEncrypt = int(textToEncrypt,2)
            ciphertext.append(encryption(textToEncrypt, n, B))
        return ciphertext

    plaintext = [ord(char) for char in plaintext]
    ciphertext = []
    for i in plaintext:
        ciphertext.append(encryption(i, n, B))

    print(f"plaintext = {plaintext}")
    print("\n")
    print(f'Ciphertext = {ciphertext}')

    return ciphertext
def RabinDecrypt(ciphertext):
    if ("[" in ciphertext) or ("]" in ciphertext):
        ciphertext = ciphertext.replace("[","")
        ciphertext = ciphertext.replace("]","")
        ciphertext = ciphertext.split(",")

    ciphertext = [int(i) for i in ciphertext]

    p = 10092003300140014003
    q = 36484957213536676883

    B = int(delete_space("daae"), 32)


    n = p * q
    if not 0 <= B < n:
        B = B%n


    upperbound = "01111010" + "00111111"
    sliceSize = -2
    while ((int(upperbound,2)**2) *(int(upperbound,2)+B)) < n:
        upperbound = "01111010" + upperbound
        sliceSize += 1

    if sliceSize >=1:
        plaintext = []
        for i in ciphertext:
            try:
                text = format(decryption(i, p, q,B),f"0{8*sliceSize}b")
                plaintext+= [text[i:i+8] for i in range(0,len(text),8)]
            except:
                plaintext +="00000000"



        plaintext = [chr(int(i,2)) for i in plaintext]
        textdecrypt= "".join(plaintext)
        return textdecrypt

    plaintext = []
    for i in ciphertext:
        plaintext.append(chr(decryption(i, p, q,B)))
    textdecrypt= "".join(plaintext)
    return textdecrypt


Cipher = RabinEncrypt("""Dies irae, dies illa,
Solvet saeclum in favilla
Teste David cum Sibylla.""")
print(f"Message = {RabinDecrypt(Cipher)}")
