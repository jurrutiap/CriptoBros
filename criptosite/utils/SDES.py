import numpy as np

def K(k):
    if len(k) == 10:
        return k
    else:
        return '1101111101'

def apply_table(inp, table):
    res = ""
    for i in table:
        res += inp[i - 1]
    return res


def left_shift(data):
    return data[1:] + data[0]


def XOR(a, b):
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res


def apply_sbox(s, data):
    row = int("0b" + data[0] + data[-1], 2)
    col = int("0b" + data[1:3], 2)
    return bin(s[row][col])[2:]


def function(expansion, s0, s1, key, message):
    left = message[:4]
    right = message[4:]
    temp = apply_table(right, expansion)
    temp = XOR(temp, key)
    l = apply_sbox(s0, temp[:4])  # noqa: E741
    r = apply_sbox(s1, temp[4:])
    l = "0" * (2 - len(l)) + l  # noqa: E741
    r = "0" * (2 - len(r)) + r
    temp = apply_table(l + r, p4_table)
    temp = XOR(left, temp)
    return temp + right


p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p4_table = [2, 4, 3, 1]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
expansion = [4, 1, 2, 3, 2, 3, 4, 1]
s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]


def generateKey(key):
    temp = apply_table(key, p10_table)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = apply_table(left + right, p8_table)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = apply_table(left + right, p8_table)
    return key1, key2


def SDESEncryption(plain_text, key):
    keys = generateKey(key)
    temp = apply_table(plain_text, IP)
    temp = function(expansion, s0, s1, keys[0], temp)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, keys[1], temp)
    CT = apply_table(temp, IP_inv)
    return CT, key


def SDESDecryption(plain_text, key):
    keys = generateKey(key)
    temp = apply_table(plain_text, IP)
    temp = function(expansion, s0, s1, keys[1], temp)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, keys[0], temp)
    PT = apply_table(temp, IP_inv)
    return PT, key