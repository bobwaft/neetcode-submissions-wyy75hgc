class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.combination = []
        def dfs(i):
            if sum(self.combination) == target:
                self.res.append(self.combination[:])
                return
            elif sum(self.combination) > target:
                res = []
                return
            if (i>=len(nums)):
                return
            self.combination.append(nums[i])
            dfs(i)
            self.combination.pop()
            dfs(i+1)
        dfs(0)
        return self.res
