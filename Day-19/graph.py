def insertNode(val):
    global Node_count
    if val in Nodes:
        print(f"{val} is alrready present in the list")
    else:
        Node_count+=1
        Nodes.append(val)
        for i in adMatrix:
            i.append(0)
        temp = [0]*Node_count
        adMatrix.append(temp)

def add_edge(e1,e2):
    if e1 not in Nodes:
        print(f"{e1} is not present")
    elif e2 not in Nodes:
        print(f"{e2} is not present")
    else:
        index1 = Nodes.index(e1)
        index2 = Nodes.index(e2)
        adMatrix[index1][index2] = 1
        adMatrix[index2][index1] = 1

def printMat(adMatrix):
    for i in adMatrix:
        for j in i:
            print(format(j),end=" ")
        print()

Nodes = []
adMatrix = []
Node_count = 0
print("Before adding node")
print(Nodes)
printMat(adMatrix)
insertNode('A')
insertNode('A')
insertNode('B')
insertNode('C')
add_edge('A','B')
add_edge('C','D')
add_edge('A','C')
print("After adding nodes")
print(Nodes)
printMat(adMatrix)

#output
'''
Before adding node
[]
A is alrready present in the list
After adding nodes
['A', 'B', 'C']
0 0 0
0 0 0
0 0 0
'''