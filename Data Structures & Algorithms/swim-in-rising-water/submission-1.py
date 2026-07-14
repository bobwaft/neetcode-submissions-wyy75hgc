class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minHeap = [(grid[0][0],0,0)]
        minCosts = {}
        res = float("inf")
        while minHeap:
            h1,r,c = heapq.heappop(minHeap)
            if (r,c) in minCosts:
                continue
            if r == rows-1 and c==cols-1:
                return h1
            minCosts[(r,c)] = h1
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (r+dr,c+dc) not in minCosts and min(r,c) >= 0 and r+dr<rows and c+dc<cols:
                    heapq.heappush(minHeap,(max(h1,grid[r+dr][c+dc]),r+dr,c+dc))
        print(minCosts)
        return -1
