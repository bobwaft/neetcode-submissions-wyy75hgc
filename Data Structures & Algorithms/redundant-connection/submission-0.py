class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(1,n+1):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self,n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = None
        unionfind = UnionFind(len(edges))
        for edge in edges:
            if not unionfind.union(edge[0],edge[1]):
                res = edge
        return res