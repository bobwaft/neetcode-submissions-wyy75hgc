class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        cache = {}
        return self.dfs(0,0,sum(nums)//2,nums,cache)

    def dfs(self,i,cur,targ,nums,cache):
        if (cur,i) in cache:
            return cache[(cur,i)]
        if i == len(nums) or cur > targ:
            cache[(cur,i)] = False
            return cache[(cur,i)]
        if cur == targ:
            cache[(cur,i)] = True
            return cache[(cur,i)]
        exclude = self.dfs(i+1,cur,targ,nums,cache)
        include = self.dfs(i+1,cur + nums[i],targ,nums,cache)
        cache[(cur,i)] = include or exclude
        return cache[(cur,i)]
        