class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(res,subset,i):
            if i >= len(nums):
                res.append(subset[:])
                return res
            subset.append(nums[i])
            res = dfs(res,subset,i+1)
            subset.pop()
            dfs(res,subset,i+1)
            return res
        res = dfs([],[],0)
        return res