class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        largest = None
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            if not largest or cur > largest:
                largest = cur
            if cur < 0:
                cur = 0
        return largest
            
                
            
            