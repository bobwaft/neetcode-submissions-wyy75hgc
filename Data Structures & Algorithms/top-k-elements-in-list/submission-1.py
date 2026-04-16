class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        mostCommonK = counter.most_common(k)
        res = [i for i,_ in mostCommonK]
        return res