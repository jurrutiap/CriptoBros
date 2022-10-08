<img align="right" src="img/cover.png" height="75">

# CriptoBros, easy to use encrypting tool

Live demo [here](http://ec2-3-129-10-141.us-east-2.compute.amazonaws.com:8000/)

This is a web-based encryption proposal developed for "Introduction to Cryptography" (Universidad Nacional de Colombia). Below you will find a walkthrough and a brief explanation of the project.

## What to expect

- **Easily encrypt and decrypt plain text**, the user can provide a key; otherwise the app will provide a random one.
- Perform **cryptoanalysis and attack** and retrieve information from encrypted texts.
- **Encrypt and decrypt images** using the Hill Image-Encryption method

## Implemented encryption methods

- [**Hill Image Encryption**](#hill-image-encryption)
- [**Shift cipher**](#shift-cipher)
- [**Multiplicative Cipher**](#multiplicative-cipher)
- **Transposition Cipher**
- [**Vigenere cipher**](#vigenere-cipher)
- [**Affine cipher**](#affine-cipher)
- **Substitution cipher**

## Hill Image Encryption
[(Back to top)](#what-to-expect)

The Hill cipher algorithm is a symmetric key algorithm which means that we can get the decryption key out of the encryption one easily. In this case, we use an Involutory Key Matrix, the reason bethind this is that the inverse of an involutory matrix is itself, making the decryption methods easier.

The result of applying Hill Image Encryption are the following:<br><br>

<img src="img/0.png" width="500px" height="auto"> | <img src="img/Encrypted.png" width="500px" height="auto"> | <img src="img/Key.png" width="500px" height="auto"> | <img src="img/Decrypted.png" width="500px" height="auto"> 
---|---|---|---
Original image | Encrypted image | Encryption key | Decrypted image

<br><br>

## Shift Cipher
[(Back to top)](#what-to-expect)

The Shift cipher (also known as Caesar cipher) works by using the modulo operator to encrypt and decrypt messages. The Shift Cipher has a key $k$, which is an integer in $\mathbb{Z}_{26}$. The encryption function is $$e_k(x) = (x+k)mod n$$ and the decryption function is $$d_k(c) = (c-k)mod n$$ were $x$ is a clear text, $c$ is an encrypted text and $n = 26$.

## Multiplicative Cipher
[(Back to top)](#what-to-expect)

The Multiplicative cipher works by multiplying each letter's value by $k \in \mathbb{Z}_{26}$. The condition for the $k$ is that it must be a relative prime to 26, i.e. [3,5,7,9,11,15,17,19,21,23,25]. The encryption function is $$e_k(x) = (x\cdot k)mod n$$ and the decryption function is $$d_k(c) = (c\cdot k^{-1})mod n$$ were $x$ is a clear text, $c$ is an encrypted text and $n = 26$.

## Vigenere cipher
[(Back to top)](#what-to-expect)

Vigenere Cipher uses polyalphabetic substitution scheme, this means it uses multiple substitutions over a single text. In the Shift Cipher, all the letters are shifted by the same amount $k$. However, Vigenere Cipher implement several Shift Ciphers, one after another. In this Cipher, the user chooses a word not longer than the clear text, and repeats it until it matches the length of the text. Then, the encryption function is applied: $$e_i(x) = (x_i+k_i)mod n$$ for every letter $i$ on the text.

To decript, the decryption function is applied: $$e_i(c) = (c_i-k_i)mod n$$ The attack on this system is done by analyzing the frecuency of each letter, and comparing it to the [table frecuency of letters in the english alphabet](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html).

## Affine Cipher
[(Back to top)](#what-to-expect)

The Affine cipher works by using the following encryption function: $$e_k(x) = (a\cdot x+b)mod n$$ where:
- $a$ and $b$ must be relative primes to 26.
- $b$ is smaller than $a$.
The affine cipher is a reinforcement to the multiplicative cipher mentioned earlier.

The decryption function is defined as:  $$e_k(x) = a^{-1}\cdot(x-b)mod n$$
