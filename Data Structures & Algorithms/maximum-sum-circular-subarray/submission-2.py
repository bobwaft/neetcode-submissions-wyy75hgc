class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            curSum = max(curSum,0)
            curSum += num
            maxSum = max(curSum,maxSum)
        if max(nums) >= 0:
            minSum = nums[0]
            curSum = 0
            for num in nums:
                curSum = min(curSum,0)
                curSum += num
                minSum = min(curSum,minSum)
            maxSum = max(maxSum,sum(nums)-minSum)
        return maxSum