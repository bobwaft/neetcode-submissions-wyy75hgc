class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        rows, cols = len(grid),len(grid[0])
        length = 1
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        while len(queue) > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
                for dr,dc in neighbors:
                    if (min(r+dr,c+dc) < 0 or r + dr == rows or c + dc == cols or
                    (r + dr, c + dc) in visited or grid[r+dr][c+dc] == 1):
                        continue
                    queue.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
            length += 1
        return -1