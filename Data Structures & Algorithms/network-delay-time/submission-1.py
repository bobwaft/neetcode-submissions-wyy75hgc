class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Convert to adjacency list
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for (u,v,t) in times:
            adj[u].append((v,t))
        
        #Dijkstra
        visited = set()
        res = 0
        minHeap = [[0,k]]

        while minHeap:
            t1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = t1
            for (n2,t2) in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(t1+t2,n2))
        if len(visited) != n:
            return -1
        return res