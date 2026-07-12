class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,cur = [],[]
        self.dfs(nums,0,res,cur)
        return res
    def dfs(self,nums,i,res,cur):
        if i>=len(nums):
            res.append(cur.copy())
            return
        cur.append(nums[i])
        self.dfs(nums,i+1,res,cur)
        cur.pop()
        while (i + 1 < len(nums) and nums[i] == nums[i+1]):
            i+=1
        self.dfs(nums,i+1,res,cur)
