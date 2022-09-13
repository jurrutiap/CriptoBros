import itertools

# function to get the inverse of a permutation
def inverPermut(perm):
    permInv = [0]*len(perm)
    for i in range(1,len(perm)+1):
        permInv[perm[i-1]-1] = i

    return permInv

# function to apply a permutation to
# a given text
def applyPermutation(text,permutation):
    permutedText = [0]*len(text)
    for i in range(len(text)):
        permutedText[permutation[i]-1] = text[i]

    permutedText = ''.join(permutedText)
    return permutedText




## PARAMETERS :
    ## text: the text to permute
    ## permutationLenght: the possible lenght of the key permutation

# We need the text to analize
# Can accept any number, but the growth is permutationLenght!
# So for any permutationLenght > 6, it's better to use the
# Hill Cryptoanalisys
def transpositionCryptoanalisys(text, permutationLenght):

    #erase any non alphabet character
    clearText = ''.join(ch for ch in text if ch.isalpha())

    # in case the lenght of the text is not divisible by the
    # lenght of the permutation, get rid of any extra
    # as to only get text in which the permutation can be applied
    permutableLenght = len(clearText)//permutationLenght

    permutableText = clearText[:permutableLenght*permutationLenght]

    # por each possible permutation of permutationLenght elements
    # WARNING: HAS FACTORIAL GROWTH
    ## FOR A LENGHT OF 7 OR MORE, USE HILL CRYPTOANALISYS ##
    for permutation in list(itertools.permutations(list(range(1,permutationLenght+1)))):

        # Skip the identity permutation
        if permutation == tuple(range(1,permutationLenght+1)):
            continue

        # create an empty string to store the possible plain text
        possibleText = ""

        # for each slice of permutableLenght in the text
        for indx in range(0,permutableLenght):

            # calculate the step
            step = indx * (permutableLenght+1)


            #and apply the possible permutation to this slice (of lenght permutable lenght)
            possibleText += applyPermutation(permutableText[step:step+permutableLenght+1],permutation)

        # calculate the inverse of the permutation used
        # (since, if we got the original plain text it means we used the inverse
        # permutation on the permuted text. So, to get the original key, calculate the
        # inverse of the inverse, the original permutation)
        usedPermutation = inverPermut(permutation)


        print(f"if the key is the permutation {usedPermutation}, \n   the text is {possibleText} \n")



text = "EESLSHSALSESLSHBLEHSYEETHRAEOS"

transpositionCryptoanalisys(text,6)


