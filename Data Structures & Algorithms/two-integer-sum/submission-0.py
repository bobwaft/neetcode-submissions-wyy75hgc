class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            if (target-nums[i] in hashTable and hashTable[target-nums[i]] != i):
                return sorted([i,hashTable[target-nums[i]]])
            hashTable[nums[i]] = i