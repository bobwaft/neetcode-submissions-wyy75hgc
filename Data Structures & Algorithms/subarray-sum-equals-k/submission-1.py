class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        res = 0
        prefixSums = {0:1}
        for num in nums:
            total += num
            res += prefixSums.get(total-k,0)
            prefixSums[total] = prefixSums.get(total,0) + 1
        
        return res