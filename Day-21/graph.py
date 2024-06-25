def add_Node(data):
    if data in graph:
        print("Node is already Present !!")
    else:
        graph[data]=[]

def add_Edge(v1,v2):
    if v1 not in graph:
        print(f"{v1} is not in graph")
    elif v2 not in graph:
        print(f"{v2} not in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print("Node is not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
            
def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print("Node is not present")
        return
    stack = []
    stack.append(node)
    while stack:
        currrent = stack.pop()
        if currrent not in visited:
            print(currrent)
            visited.add(currrent)
            for i in graph[currrent]:
                stack.append(i)



visited = set()

graph = {}
print("Before")
print(graph)
print("After")
add_Node('A')
add_Node('B')
add_Edge('A','B')
add_Edge('A','C')
add_Node('C')
add_Edge('A','C')
print(graph)
print("Recursive Traversal")
DFS('A',visited,graph)
print("Stack Traversal")
DFSiterative('A',graph)

#OUTPUT
'''
Before
{}
After
C not in graph
{'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
Recursive Traversal
A
B
C
Stack Traversal
A
C
B
'''