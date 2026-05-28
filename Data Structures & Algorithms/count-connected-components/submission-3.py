class DFS:
    def __init__(self, n):
        self.comps = n
        self.parent = list(range(n))
        self.rank = [0]*n

    def findparent(self, node):
        if self.parent[node] != node:
           self.parent[node] = self.findparent(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.findparent(u)
        pv = self.findparent(v)
        if pu == pv:
            return False;
        self.comps -= 1
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True;

    def components(self):
        return self.comps;

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dfs = DFS(n)
        for u,v in edges:
            dfs.union(u,v)
        n = dfs.components()
        return n;