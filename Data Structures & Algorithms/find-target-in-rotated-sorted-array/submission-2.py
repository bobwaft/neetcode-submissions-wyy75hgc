class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        best = -1
        while l < r:
            m = (l+r)//2
            if best == -1 or nums[m] < nums[best]:
                best = m
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
        if best == -1 or nums[l] < nums[best]:
            best = l
        if best == 0:
            return self.binSearch(0,len(nums)-1,target,nums)
        else:
            return max(self.binSearch(0,best-1,target,nums),self.binSearch(best,len(nums)-1,target,nums))     
    
    def binSearch(self,l,r,targ,nums):
        while l <= r:
            m = (l+r)//2
            if targ > nums[m]:
                l = m + 1
            elif targ < nums[m]:
                r = m - 1
            else:
                return m
        return -1

