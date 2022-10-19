import matplotlib.pyplot as plt
from random import randrange
import json

matrixAlph = list()


def genPermutation():
    permutation = list()
    for i in range(10):
        permutation.append(str(randrange(10)))
    return permutation


def initializeMatrix():
    del matrixAlph[:]
    for i in range(10):
        aux = list()
        for j in range(20):
            aux.append(j)
        matrixAlph.append(aux)


def loadPermutation(permut):
    for i in range(len(permut)):
        for j in range(20):
            matrixAlph[i][j] = (int(permut[i]) + matrixAlph[i][j]) % 26


def plotGraph(x, y):
    n = 10
    vect = None
    edges = set()
    curr = (x, y)
    for i in range(n + 1):
        next = (curr[0] + 1, curr[1] + i)
        segment = (curr, next)
        curr = next
        edges.add(segment)
    dirA = edges
    edges = set()
    for segment in dirA:
        last = segment[1]
        edgetm = set()
        curr = (*last, n)
        for i in range(n + 1):
            next = (curr[0] + 1, curr[1] + i)
            segment = (curr, next)
            curr = next
            edgetm.add(segment)
        temp = edgetm
        edges = edges.union(temp)
    dirB = edges
    edges = set()
    for segment in dirB:
        last = segment[1]
        pendiente = segment[1][1] - segment[0][1]
        edgetm = set()
        curr = (*last, pendiente)
        for i in range(n + 1):
            next = (curr[0] + 1, curr[1] + i)
            segment = (curr, next)
            curr = next
            edgetm.add(segment)
        temp = edgetm
        edges = edges.union(temp)
    dirC = edges
    total = set()
    vect = ((total.union(dirA)).union(dirB)).union(dirC)
    return vect


def createGraph(x,y,mode):
    vect= plotGraph(x, y)
    plt.axis('equal')
    for segment in vect:
        p0 = segment[0]
        p1 = segment[1]
        if(mode==1):
            xs = [p0[0]+x, p1[0]+x]
            ys = [p0[1]+y, p1[1]+y]
        else:
            xs = [p0[0] , p1[0] ]
            ys = [p0[1] , p1[1] ]
        plt.xlim(x-5, x + 15)
        plt.ylim(y-5, y + 20)
        plt.plot(xs, ys, color='r', linestyle="-", marker='o',
                linewidth=1, markersize=2)

def getVector(x, y):
    n = 10
    edges = set()
    curr = (x, y)
    for i in range(n + 1):
        next = (curr[0] + 1, curr[1] + i)
        segment = (curr, next)
        curr = next
        edges.add(segment)
    dirA = edges
    edges = set()
    for segment in dirA:
        last = segment[1]
        edgetm = set()
        curr = (*last, n)
        for i in range(n + 1):
            next = (curr[0] + 1, curr[1] + i)
            segment = (curr, next)
            curr = next
            edgetm.add(segment)
        temp = edgetm
        edges = edges.union(temp)
    dirB = edges
    edges = set()
    for segment in dirB:
        last = segment[1]
        pendiente = segment[1][1] - segment[0][1]
        edgetm = set()
        curr = (*last, pendiente)
        for i in range(n + 1):
            next = (curr[0] + 1, curr[1] + i)
            segment = (curr, next)
            curr = next
            edgetm.add(segment)
        temp = edgetm
        edges = edges.union(temp)
    dirC = edges
    total = set()
    vect = ((total.union(dirA)).union(dirB)).union(dirC)
    return vect


def count(x, y, path):
    count = 0
    for segment in path:
        if (x, y) == segment[1]:
            count += 1
    return count


def increaseAlph(x, y):
    pathh = getVector(x, y)
    for i in range(10):
        for j in range(20):
            n = count(i, j, pathh)  # n es lo que se desplaza
            matrixAlph[i][j] = (matrixAlph[i][j] + n) % 26


def encryptGammaPentagonal(plain_text):
    plain_text = plain_text.lower()
    env = setEnviroment(10, 5)
    text = plain_text
    try:
        cifrado = ""
        text = list(text)
        k = len(text)
        while k > 0:
            for i in range(10):
                for j in range(20):
                    # print(i,j, k)
                    if (chr(matrixAlph[i][j] + 97) == text[len(text) - k]):
                        cifrado += ('(' + str(i) + ',' + str(j) + ');')
                        k -= 1
                    if (k == 0):
                        break
                if (k == 0):
                    break
        return cifrado, json.dumps(matrixAlph)

    except:
        print('Something bad ocurred, try again')


def decryptGammaPentagonal(a, matrixAlph):
    a = a[0:len(a) - 1]
    try:
        text = a.split(";")
        descifrado = ""
        for coord in text:
            coords = coord.split(',')
            descifrado += chr(matrixAlph[int(coords[0][1:])][int(coords[1][:-1])] + 97)
        return descifrado.upper(), matrixAlph

    except Exception as e:
        print(e)
        print('Something bad ocurred, try again')


def setEnviroment(x, y):
    global matrixAlph
    permutation = list()
    permutation = genPermutation()
    matrixAlph = list()
    initializeMatrix()
    loadPermutation(permutation)
    createGraph(x,y,0)
    return x, y, permutation
