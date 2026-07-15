class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[],[]]
        optimalCost = self.buildMSTExclude(n,edges,-1)
        for i in range(len(edges)):
            includeCost,excludeCost = self.buildMSTInclude(n,edges,i), self.buildMSTExclude(n,edges,i)
            if excludeCost > optimalCost:
                res[0].append(i)
            elif includeCost == optimalCost:
                res[1].append(i)
        return res
        
    def buildMSTExclude(self,n,edges,force):
        minHeap = []
        i = 0
        for n1,n2,w in edges:
            if i != force:
                heapq.heappush(minHeap,[w,n1,n2])
            i += 1
        uf = UnionFind(n)
        res = 0
        mst = []
        while minHeap:
            w,n1,n2 = heapq.heappop(minHeap)
            if not uf.union(n1,n2):
                continue
            res += w
            mst.append([n1,n2,w])
        if len(mst) < n - 1:
            return float("inf")
        return res

    def buildMSTInclude(self,n,edges,force):
        minHeap = []
        i = 0
        for n1,n2,w in edges:
            if i != force:
                heapq.heappush(minHeap,[w,n1,n2])
            i += 1
        uf = UnionFind(n)
        forcen1,forcen2,forcew = edges[force] 
        uf.union(forcen1,forcen2)
        res = forcew
        while minHeap:
            w,n1,n2 = heapq.heappop(minHeap)
            if not uf.union(n1,n2):
                continue
            res += w
        return res