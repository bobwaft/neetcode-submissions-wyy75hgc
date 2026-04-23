class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        def dfs(r,c,grid,visited):
            if (r,c) in cache:
                return cache[(r,c)]
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == 1:
                cache[(r,c)] = 0
                return cache[(r,c)]
            if r == rows - 1 and c == cols - 1:
                cache[(r,c)] = 1
                return cache[(r,c)]
            visited.add((r,c))
            cache[(r,c)] = (dfs(r+1,c,grid,visited) + dfs(r,c+1,grid,visited))
            visited.remove((r,c))
            return cache[(r,c)]
        return dfs(0,0,obstacleGrid,set())