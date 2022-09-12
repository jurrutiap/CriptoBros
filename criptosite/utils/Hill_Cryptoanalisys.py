import numpy as np
import globals as g

INVERTIBLENUMBERS = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}


# Fill a sizeOfKey x sizeOfKey matrix for the plain text
def FillPlainText(sizeOfKey):
    knownPlainText = []

    #while we have less than sizeOfKey rows in the knownPlainText matrix
    while len(knownPlainText) < sizeOfKey:

        #ask for a row of sizeOfKey elements of plain text
        PlainRow = input(f"insert plain text row number {len(knownPlainText) + 1} ").split()

        #check if the plain text was given as numbers or text
        text = False
        for i in PlainRow:
            if i.isalpha():
                text = True

        #if text, convert to numbers
        if text:
            for x in PlainRow:
                PlainRow = g.chartonum(x.upper())
        #else, just add the numbers to a list
        else:
            PlainRow = [int(x) for x in PlainRow]

        # if the row isn't exactly sizeOfKey in lenght
        # throw error and repeat
        if len(PlainRow) != sizeOfKey:
            print("Error")
            print(f"row must be of lenght {sizeOfKey}")
            continue

        #add the row to the knownPlainText matrix
        knownPlainText.append(PlainRow)

    #convert the 2D array to a matrix
    knownText = np.matrix(knownPlainText)

    return knownText

# Fill a sizeOfKey x sizeOfKey matrix for the cipher text
def FillCipherText(sizeOfKey):
    knownCipherText = []

    #while we have less than sizeOfKey rows in the knownCipherText matrix
    while len(knownCipherText) < sizeOfKey:

        #ask for a row of sizeOfKey elements of cipher text
        CipherRow = input(f"insert cipher text row number {len(knownCipherText) + 1} ").split()

        #check if the cipher text was given as numbers or text
        text = False
        for i in CipherRow:
            if i.isalpha():
                text = True


        #if text, convert to numbers
        if text:
            for x in CipherRow:
                CipherRow = g.chartonum(x.upper())

        #else, just add the numbers to a list
        else:
            CipherRow = [int(x) for x in CipherRow]


        # if the row isn't exactly sizeOfKey in lenght
        # throw error and repeat
        if len(CipherRow) != sizeOfKey:
            print("Error")
            print(f"row must be of lenght {sizeOfKey} ")
            continue

        #add the row to the knownCipherText matrix
        knownCipherText.append(CipherRow)

    #convert the 2D array to a matrix
    knownText = np.matrix(knownCipherText)


    return knownText

# Function to calculate the minor matrix of an element
def MatrixMinor(matrix,row,column):
    minor = matrix[np.array(list(range(row))+list(range(row+1,matrix.shape[0])))[:,np.newaxis],
               np.array(list(range(column))+list(range(column+1,matrix.shape[1])))]

    return minor


# Function to calculate the adjoint matrix
def MatrixAdjoint(matrix, size):

    adj = [[] for x in range(size)]
    for i in range(size):
        for j in range(size):
            adj[i].append((-1)**(i+j) * round(np.linalg.det(MatrixMinor(matrix,j,i))))

    return np.array(adj)


#sizeOfKey = the n of the nxn matrix of the key (since the matrix
# has to be a square matrix)
def HillCryptoanalisys(sizeOfKey):

    while True:

        #Ask for plain text
        knownPlainText = FillPlainText(sizeOfKey)

        #check if the matrix is invertible (mod 26)
        # the matrix is invertible if its determinant has inverse mod 26
        if round(np.linalg.det(knownPlainText))%26 not in list(INVERTIBLENUMBERS.keys()):

            #if the matrix is not invertible, throw error and ask for another plain text
            print("Error, non invertible matrix")
            continue
        break

    #Calculate the matrix inverse (mod 26) of the plain text matrix
    knownPlainTextInverse = (INVERTIBLENUMBERS[round(np.linalg.det(knownPlainText))%26] * MatrixAdjoint(knownPlainText,sizeOfKey))%26

    #Ask for cipher text
    knownCipherText = FillCipherText(sizeOfKey)

    #multiply both matrixes
    key = np.matmul(knownPlainTextInverse, knownCipherText)%26

    #small function to convert each element to a letter
    numToChar = lambda i: chr(i+97).upper()

    #change the number matrix to a letter matrix
    alphaKey = np.vectorize(numToChar)(key)

    return alphaKey


print(HillCryptoanalisys(2))




