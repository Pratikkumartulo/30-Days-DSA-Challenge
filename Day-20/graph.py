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

#OUTPUT
'''
Before
{}
After
C not in graph
{'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
'''