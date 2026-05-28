class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        l = 0
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                length = min(length,r-l+1)
                curSum -= nums[l]
                l+=1
        return 0 if length == float("inf") else length