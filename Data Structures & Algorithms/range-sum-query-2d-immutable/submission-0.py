class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cols = len(matrix[0])
        rows = len(matrix)
        self.prefixes = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            rowSum = 0
            for col in range(cols):
                rowSum += matrix[row][col]
                self.prefixes[row][col] = rowSum + self.prefixes[row-1][col] if row > 0 else rowSum
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefixes[row2][col2]
        res -= self.prefixes[row2][col1-1] if col1 > 0 else 0
        res -= self.prefixes[row1-1][col2] if row1 > 0 else 0
        res += self.prefixes[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)