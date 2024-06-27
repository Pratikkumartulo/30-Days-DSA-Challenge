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

def delete_Node(node):
    if node not in graph:
        print(f"{node} is not present in the graph")
    else:
        graph.pop(node)
        for i in graph:
            lst = graph[i]
            if node in lst:
                lst.remove(node)
def delete_edge(v1,v2):
    if v1 not in graph:
        print(f"{v1} not in graph")
    elif v2 not in graph:
        print(f"{v2} not in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


graph = {}
print("Before Deleting")
print(graph)
add_Node('A')
add_Node('B')
add_Edge('A','B')
add_Edge('A','C')
add_Node('C')
add_Node('D')
add_Edge('A','C')
add_Edge('B','D')
add_Edge('A','D')
add_Edge('C','D')
print("Graph Previously")
print(graph)
print("After deleting Node A")
delete_Node('A')
print(graph)
print("After deleting Edge C-D")
delete_edge('C','D')
print(graph)
#OUTPUT
'''
Before Deleting
{}
C not in graph
Graph Previously
{'A': ['B', 'C', 'D'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'A', 'C']}
After deleting Node A
{'B': ['D'], 'C': ['D'], 'D': ['B', 'C']}
After deleting Edge C-D
{'B': ['D'], 'C': [], 'D': ['B']}
'''