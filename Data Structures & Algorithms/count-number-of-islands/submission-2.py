class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        def dfs(grid,r,c,island):
            rows,cols = len(grid),len(grid[0])
            if (min(c,r) < 0 or c == cols or r == rows or
            (r,c) in island or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            island.add((r,c))
            dfs(grid,r-1,c,island)
            dfs(grid,r+1,c,island)
            dfs(grid,r,c-1,island)
            dfs(grid,r,c+1,island)
            return island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island = dfs(grid,i,j,set())
                if island:
                    islands.append(island)
        return len(islands)