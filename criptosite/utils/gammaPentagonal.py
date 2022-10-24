import matplotlib.pyplot as plt
import random

class Found(Exception): pass

# Parse permutation
def parsePermutation(perm):
    try:
        poss = [int(x) for x in perm.replace('[','').replace(']','').split(',')]
        if (len(poss) != 10) or not all(isinstance(n, int) for n in poss):
            raise
    except:
        poss = generatePermutation()
    return poss

# Parse initial coords
def parseCoords(perm):
    try:
        poss = [int(x) for x in perm.split(',')]
        if (len(poss) != 2) or not all(isinstance(n, int) for n in poss):
            raise
    except:
        poss = [0,0]
    return poss

# Generate random perm (size=10)
def generatePermutation():
    perm=[]
    for i in range(10):
        perm.append(random.randint(0, 25))
    return perm

# Generate encription Graph (size=26x26)
def generateGraph(start_x, start_y):
    graph = {}
        
    #1ST GEN
    slope = 0
    x = start_x
    y = start_y
    graph[(start_x, start_y)] = []
    while x < 26 and y < 26:
        if (x+1, y+slope) in graph.keys():
            graph[(x+1, y+slope)].append(slope)
        else:
            graph[(x+1, y+slope)]=[slope]
        x+=1
        y+=slope
        slope+=1
    first_gen = list(graph.keys())
    
    
    #2ND GEN
    # queue stores the 2ND GEN nodes
    queue=[]
    for key in first_gen:
        slope = 0
        x=key[0]
        y=key[1]
        if x < 26 and y < 26:
            while x < 26 and y < 26:
                if (x+1, y+slope) in graph.keys():
                    graph[(x+1, y+slope)].append(slope)
                else:
                    graph[(x+1, y+slope)]=[slope]
                queue.append((x+1, y+slope))
                x+=1
                y+=slope
                slope+=1
    
    
    #3RD GEN, slope no higher than parent's slope
    while len(queue)!= 0:
        (x, y)=queue[0]
        coord_slopes = graph[(x, y)]
        max_slope=max(coord_slopes)
        if x < 26 and y < 26:
            for slope in range(0, max_slope+1):
                if (x+1, y+slope) in graph.keys():
                    graph[(x+1, y+slope)].append(slope)
                else:
                    graph[(x+1, y+slope)]=[slope]
                x+=1
                y+=slope
                if x>=26 or y>=26:
                    break
        queue.pop(0)
    return graph

def genEquivClass(permutation, graph):

    # Calculate slope overall weights
    weight = {}
    for coord in graph.keys():
        if coord[0]+coord[1] in weight.keys():
            weight[coord[0]+coord[1]] += len(graph[(coord[0],coord[1])])
        else:
            weight[coord[0]+coord[1]] = len(graph[(coord[0],coord[1])])

    # Create letter matrix
    arrangement = [[chr(x) for x in range(97,123)] for y in range(10)]

    # Shift matrix w/ perm, then add weights to each letter
    for column in range(0, len(arrangement)):
        arrangement[column] = [chr(ord(x)+permutation[column]) for x in arrangement[column]]
        for row in range(0, len(arrangement[column])):
            try:
                arrangement[column][row] = chr(((ord(arrangement[column][row])-97 + weight[column + row])%26)+97)
            except:
                arrangement[column][row] = chr(((ord(arrangement[column][row])-97)%26)+97)

    return arrangement

def encript(text, arrangement):
    # Parse clean text
    tokens = list(filter((' ').__ne__, [x for x in ''.join([i for i in text if i.isalpha()]).lower()]))
    result = ''
    counter = 0

    for letter in range(0, len(tokens)):
        start = letter % 10
        try:
            for i in range(0, len(arrangement)):
                for j in range(0, len(arrangement[i])):
                    if arrangement[(i+start) % 10][j] ==tokens[letter]:
                        raise Found
        except Found:
            result += f'({(i+start) % 10},{j});'
            counter += 1
    #print(f'{counter}/{len(tokens)}')
    return result

def decript(encripted, permutation, graph):
    arrangement = genEquivClass(permutation, graph)
    text = encripted.replace('(', '').replace(')', '').split(";")[:-1]
    clear_text = ''
    for letter in text:
        coord = letter.split(',')
        clear_text += arrangement[int(coord[0])][int(coord[1])]
    return clear_text.upper()
    
def draw_perm(arrangement, permutation):
    plt.figure(figsize=(10,6))
    plt.style.use('classic')
    current = 0
    for n in range(0, len(arrangement)):
        for i in range(0, 26):
            letter = arrangement[n][i]
            plt.text(current, i, letter, fontsize=10, color="black", verticalalignment ='bottom', horizontalalignment ='center') 
        current+=1           
            
    plt.title(f"Permutation: {str(permutation)}", fontsize=12)
    plt.xlim(-0.5, 9.2)
    plt.ylim(-0.5, 26.5)
    for a in range(0, 55):
        for b in range(0, 27, 5):
            plt.plot(a*0.2, b, marker="_", markersize = 3, color="#BABABA")
    plt.savefig("criptosite/criptosite/static/img/GP_perm.png")


def draw_graph(graph, x, y):
    plt.figure(figsize=(10,6))
    plt.style.use('classic')
    plt.title(f"Graph starting at ({x}, {y})", fontsize=12)

    if x <=0:
        plt.xlim(x-0.5, 10.2)
        plt.plot([x-1, 10], [0, 0], color="red")
    else:
        plt.xlim(x-0.5, x+10)
        plt.plot([-1, 10], [0, 0], color="red")
        
    if y <=0:
        plt.ylim(y-0.5, 26)
        plt.plot([0, 0], [y-1, 26], color="red")
    else:
        plt.ylim(y-0.5, y+26)
        plt.plot([0, 0], [-1, 26], color="red")

    for a in range(x-1, x+11):
        for b in range(y-1, y+27):
            plt.plot(a, b, marker=".", markersize = 3, color="#BABABA")

            
    coord = list(graph.keys())
    for i in coord:
        x_coord=i[0]
        y_coord=i[1]
        for slope in graph[i]:
            plt.plot([x_coord-1, x_coord], [y_coord-slope, y_coord],  marker = 'o', markersize = 5)

    plt.plot(x, y, marker="*", markersize = 10, color="red")
    plt.savefig("criptosite/criptosite/static/img/GP_graph.png")

if __name__ == "__main__":
    # Encript
    text = str(input())
    perm = parsePermutation(str(input()))
    print(perm)
    initial_coords = parseCoords(str(input()))
    graph = generateGraph(initial_coords[0],initial_coords[1])
    equiv = genEquivClass(perm, graph)
    ciphered = encript(text, equiv)
    print(ciphered)
    draw_perm(equiv, perm)
    draw_graph(graph, initial_coords[0],initial_coords[1])

    # Decript
    encripted = str(input())
    perm = parsePermutation(str(input()))
    print(perm)
    initial_coords = parseCoords(str(input()))
    graph = generateGraph(initial_coords[0],initial_coords[1])
    print(decript(encripted, perm, graph))