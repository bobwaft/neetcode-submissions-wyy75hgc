class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(len(edges)):
            s,e = edges[i][0],edges[i][1]
            adj[s].append((succProb[i],e))
            adj[e].append((succProb[i],s))
        
        maxHeap = [(-1,start_node)]
        visited = set()
        while maxHeap:
            p1,n1 = heapq.heappop(maxHeap)
            p1 *= -1
            if n1 in visited:
                continue
            if n1 == end_node:
                return p1
            visited.add(n1)
            for p2,n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(maxHeap,(-p2*p1,n2))
        return 0