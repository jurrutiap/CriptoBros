import numpy as np
import globals as g

INVERTIBLENUMBERS = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}

def FillPlainText(sizeOfKey):
    knownPlainText = []
    while len(knownPlainText) < sizeOfKey:
        PlainRow = input(f"insert plain text row number {len(knownPlainText) + 1} ").split()

        text = False
        for i in PlainRow:
            if i.isalpha():
                text = True

        if text:
            for x in PlainRow:
                PlainRow = g.chartonum(x.upper())
        else:
            PlainRow = [int(x) for x in PlainRow]

        if len(PlainRow) != sizeOfKey:
            print("Error")
            print(f"row must be of lenght {sizeOfKey}")
            continue

        knownPlainText.append(PlainRow)

    knownText = np.matrix(knownPlainText)

    return knownText

def FillCipherText(sizeOfKey):
    knownCipherText = []

    while len(knownCipherText) < sizeOfKey:
        CipherRow = input(f"insert cipher text row number {len(knownCipherText) + 1} ").split()

        text = False
        for i in CipherRow:
            if i.isalpha():
                text = True

        if text:
            for x in CipherRow:
                CipherRow = g.chartonum(x.upper())
        else:
            CipherRow = [int(x) for x in CipherRow]
        if len(CipherRow) != sizeOfKey:
            print("Error")
            print(f"row must be of lenght {sizeOfKey} ")
            continue

        knownCipherText.append(CipherRow)

    knownText = np.matrix(knownCipherText)


    return knownText

def MatrixMinor(matrix,row,column):
    minor = matrix[np.array(list(range(row))+list(range(row+1,matrix.shape[0])))[:,np.newaxis],
               np.array(list(range(column))+list(range(column+1,matrix.shape[1])))]

    return minor

def MatrixAdjoint(matrix, size):

    adj = [[] for x in range(size)]
    for i in range(size):
        for j in range(size):
            adj[i].append((-1)**(i+j) * round(np.linalg.det(MatrixMinor(matrix,j,i))))

    return np.array(adj)



def HillCryptoanalisys(sizeOfKey):

    while True:
        knownPlainText = FillPlainText(sizeOfKey)
        if round(np.linalg.det(knownPlainText))%26 not in list(INVERTIBLENUMBERS.keys()):
            print("Error, non invertible matrix")
            continue
        break

    knownPlainTextInverse = (INVERTIBLENUMBERS[round(np.linalg.det(knownPlainText))%26] * MatrixAdjoint(knownPlainText,sizeOfKey))%26

    knownCipherText = FillCipherText(sizeOfKey)

    key = np.matmul(knownPlainTextInverse, knownCipherText)%26

    return key


print(HillCryptoanalisys(2))




