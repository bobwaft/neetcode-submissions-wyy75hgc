class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            if total - prefix - nums[i] == prefix:
                return i
            prefix += nums[i]
        return -1