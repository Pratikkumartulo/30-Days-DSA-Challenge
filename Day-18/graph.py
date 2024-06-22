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
def printMat(adMatrix):
    for i in adMatrix:
        for j in i:
            print(j,end=" ")
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