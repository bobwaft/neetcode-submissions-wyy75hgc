class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        rotten = set()
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    rotten.add((i,j))

        rows, cols = len(grid),len(grid[0])

        while len(queue) > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                grid[r][c] = 2
                for dr,dc in neighbors:
                    if (min(r+dr,c+dc)<0 or r+dr == rows or c+dc == cols or 
                    (r+dr,c+dc) in rotten or grid[r+dr][c+dc] != 1):
                        continue
                    queue.append((r+dr,c+dc))
                    rotten.add((r+dr,c+dc))
            if len(queue) == 0: 
                break
            time +=1
        for row in grid:
            if 1 in row:
                return -1
        return time
