class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            nextRes = []
            for p in res:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    nextRes.append(pCopy)
            res = nextRes
        return res