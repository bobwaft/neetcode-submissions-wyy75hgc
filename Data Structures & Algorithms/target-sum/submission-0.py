class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        return self.dfs(0,0,nums,target,cache)
    def dfs(self,i,cur,nums,target,cache):
        if (i,cur) in cache:
            return cache[(i,cur)]
        if i == len(nums):
            if cur == target:
                cache[(i,cur)] = 1
                return cache[(i,cur)]
            cache[(i,cur)] = 0
            return cache[(i,cur)]
        cache[(i,cur)] = self.dfs(i+1,cur-nums[i],nums,target,cache) + self.dfs(i+1,cur+nums[i],nums,target,cache)
        return cache[(i,cur)]