class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        best = 1001
        while l < r:
            m = (l+r)//2
            best = min(best,nums[m])
            if nums[m] < nums[r]:
                r = m-1
            elif nums[m] > nums[r]:
                l = m+1
        best = min(best,nums[l])
        return best
