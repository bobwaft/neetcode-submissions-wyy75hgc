class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                n = num
                count = 1
                while n+1 in nums:
                    n = n+1
                    count += 1
                res = max(res,count)
        return res
