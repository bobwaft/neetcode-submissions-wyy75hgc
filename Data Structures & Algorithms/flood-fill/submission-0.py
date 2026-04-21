class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image,r,c,color,prevColor):
            rows = len(image)
            cols = len(image[0])
            if (min(r,c) < 0 or r >= rows or c >= cols or image[r][c] != prevColor
            or image[r][c] == color):
                return image
            image[r][c] = color
            dfs(image,r-1,c,color,prevColor)
            dfs(image,r+1,c,color,prevColor)
            dfs(image,r,c-1,color,prevColor)
            dfs(image,r,c+1,color,prevColor)
            return image
        return dfs(image,sr,sc,color,image[sr][sc])