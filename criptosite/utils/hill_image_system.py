import imageio
import numpy as np

#Codigo base: https://github.com/KhaledMoataz/Hill-Cipher---Image-Encryption/blob/master/Explanation%20%26%20Results.pdf

def encrypt_img():
    #Leer imagen y transformarla en cuadrada

    img = imageio.imread('criptosite/static/img/clean.png')
    ##dimensiones de la imagen
    l = img.shape[0]
    w = img.shape[1]
    n = max(l,w)

    #crear matriz de 0's
    if n%2:
        n = n + 1
    img2 = np.zeros((n,n,3))
    #dimension cuadrada
    img2[:l,:w,:] += img 

    #Generar la llave (matriz involutiva)
    Mod = 256
    k = 23                                                          #Llave

    d = np.random.randint(256, size = (int(n/2),int(n/2)))          #Matriz A22
    I = np.identity(int(n/2))                                       #Matriz identidad
    a = np.mod(-d,Mod)                                              #A11 = -A22
    b = np.mod((k * np.mod(I - a,Mod)),Mod)                         #A12 = K(I-A11)
    k = np.mod(np.power(k,127),Mod)                                 #1/k
    c = np.mod((I + a),Mod)                                         #A21 = (1/k)(I+A11)
    c = np.mod(c * k, Mod)

    #concatenar las submatrices
    A1 = np.concatenate((a,b), axis = 1)
    A2 = np.concatenate((c,d), axis = 1)
    A = np.concatenate((A1,A2), axis = 0)
    Test = np.mod(np.matmul(np.mod(A,Mod),np.mod(A,Mod)),Mod)

    #Salvar la matriz llave como imagen
    key = np.zeros((n + 1, n))
    key[:n, :n] += A
    #La ultima fila carga la informacion del size original
    key[-1][0] = int(l / Mod)
    key[-1][1] = l % Mod
    key[-1][2] = int(w / Mod)
    key[-1][3] = w % Mod
    imageio.imwrite("criptosite/static/img/Key.png", key)

    #Encriptar
    Enc1 = (np.matmul(A % Mod,img2[:,:,0] % Mod)) % Mod
    Enc2 = (np.matmul(A % Mod,img2[:,:,1] % Mod)) % Mod
    Enc3 = (np.matmul(A % Mod,img2[:,:,2] % Mod)) % Mod

    #flatten y concatenar
    Enc1 = np.resize(Enc1,(Enc1.shape[0],Enc1.shape[1],1))
    Enc2 = np.resize(Enc2,(Enc2.shape[0],Enc2.shape[1],1))
    Enc3 = np.resize(Enc3,(Enc3.shape[0],Enc3.shape[1],1))
    Enc = np.concatenate((Enc1,Enc2,Enc3), axis = 2)                #Enc = A * image

    imageio.imwrite('criptosite/static/img/Encrypted.png',Enc)

def decript_img():
    Mod = 256
    Enc = imageio.imread('criptosite/static/img/Encrypted.png') 
    # Recuperar la llave y las dimensiones originales
    A = imageio.imread('criptosite/static/img/Key.png')
    l = A[-1][0] * Mod + A[-1][1]
    w = A[-1][2] * Mod + A[-1][3]
    A = A[0:-1]
    
    #Desencriptar
    Dec1 = (np.matmul(A % Mod,Enc[:,:,0] % Mod)) % Mod
    Dec2 = (np.matmul(A % Mod,Enc[:,:,1] % Mod)) % Mod
    Dec3 = (np.matmul(A % Mod,Enc[:,:,2] % Mod)) % Mod

    #flatten y concatenar
    Dec1 = np.resize(Dec1,(Dec1.shape[0],Dec1.shape[1],1))
    Dec2 = np.resize(Dec2,(Dec2.shape[0],Dec2.shape[1],1))
    Dec3 = np.resize(Dec3,(Dec3.shape[0],Dec3.shape[1],1))
    Dec = np.concatenate((Dec1,Dec2,Dec3), axis = 2)                #Dec = A * Enc

    #resize a las dimensiones originales
    Final = Dec[:l,:w,:]

    imageio.imwrite('criptosite/static/img/Decrypted.png',Final)

if __name__ == "__main__":
    encrypt_img()
    decript_img()