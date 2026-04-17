class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        longest = 1
        current = 1
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                current += 1
            else:
                current = 1
            if current >= longest:
                longest = current
            print(current)
        return longest

