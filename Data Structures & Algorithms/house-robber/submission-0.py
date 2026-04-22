class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i,nums):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            res = 0
            res += max(nums[i] + dfs(i+2,nums),dfs(i+1,nums))
            cache[i] = res
            return cache[i]
        return dfs(0,nums)