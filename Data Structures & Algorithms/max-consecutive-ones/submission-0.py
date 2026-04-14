class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > res:
                    res = count
            else:
                count = 0
        return res
            