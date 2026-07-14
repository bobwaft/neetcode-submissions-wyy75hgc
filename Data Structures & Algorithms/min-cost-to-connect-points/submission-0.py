class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []
            x1,y1 = points[i]
            for j in range(len(points)):
                if j != i:
                    x2,y2 = points[j]
                    weight = abs(x1-x2) + abs(y1-y2)
                    adj[i].append((weight,j))

        minHeap = []
        for weight,point in adj[0]:
            heapq.heappush(minHeap,(weight,0,point))

        visited = set([0])
        res = 0
        while minHeap:
            w1,src,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res += w1
            for w2,n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w2,n1,n2))
        return res