class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for n in nums:
            nextRes = []
            for p in res:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    if pCopy not in nextRes:
                        nextRes.append(pCopy)
            res = nextRes
            print(res)
        return res