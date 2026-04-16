class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in matrix:
            res.extend(i)
        l = 0
        r = len(res) - 1
        print(res)
        while l <= r:
            m = (l + r) // 2
            if (target < res[m]):
                r = m - 1
            elif (target > res[m]):
                l = m + 1
            else:
                return True
        return False