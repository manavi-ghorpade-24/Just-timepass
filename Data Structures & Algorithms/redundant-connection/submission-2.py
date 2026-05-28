class DSU:
    def __init__(self, n):
        self.comps = n
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    
    def find(self, node):
        if self.parent[node]!= node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u,v in edges:
            if dsu.union(u,v) == False:
                return [u,v]
        