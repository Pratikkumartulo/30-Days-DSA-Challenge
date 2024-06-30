'''
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

'''
'''
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
'''
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.component_count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.component_count -= 1
            return True
        return False

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        # To count edges that are added
        edges_added = 0
        
        # First, add all type 3 edges
        for edge in edges:
            if edge[0] == 3:
                if uf_alice.union(edge[1], edge[2]):
                    uf_bob.union(edge[1], edge[2])
                    edges_added += 1
        
        # Add type 1 edges for Alice
        for edge in edges:
            if edge[0] == 1:
                if uf_alice.union(edge[1], edge[2]):
                    edges_added += 1
        
        # Add type 2 edges for Bob
        for edge in edges:
            if edge[0] == 2:
                if uf_bob.union(edge[1], edge[2]):
                    edges_added += 1
        
        # Check if both graphs are fully traversable
        if uf_alice.component_count > 2 or uf_bob.component_count > 2:
            return -1
        
        # Maximum edges that can be removed
        return len(edges) - edges_added

