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

def deleteNode(node):
    global Node_count
    if node not in Nodes:
        print("Given node not present in Nodes")
    else:
        Node_count-=1
        index = Nodes.index(node)
        Nodes.remove(node)
        adMatrix.pop(index)
        for i in adMatrix:
            i.pop(index)

def deleteEdge(v1,v2):
    if v1 not in Nodes:
        print(f"{v1} is not present")
    elif v2 not in Nodes:
        print(f"{v2} is not present")
    else:
        index1 = Nodes.index(v1)
        index2 = Nodes.index(v2)
        adMatrix[index1][index2] = 0
        adMatrix[index2][index1] = 0


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
add_edge('C','B')
add_edge('A','C')
print("After adding nodes")
print(Nodes)
printMat(adMatrix)
print("After deleting A")
deleteNode('A')
print(Nodes)
printMat(adMatrix)
print("After deleting edge BC")
deleteEdge('B','C')
print(Nodes)
printMat(adMatrix)

#output
'''
Before adding node
[]
A is alrready present in the list
After adding nodes
['A', 'B', 'C']
0 1 1
1 0 1
1 1 0
After deleting A
['B', 'C']
0 1
1 0
After deleting edge BC
['B', 'C']
0 0
0 0
'''