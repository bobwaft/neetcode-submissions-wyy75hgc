class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatBanana(k,piles,h):
            for i in piles:
                h -= math.ceil(i/k)
            return h>=0
        l = 1
        r = max(piles)
        res = []
        while (l <= r):
            m = (l+r)//2
            print(l,m,r)
            if canEatBanana(m,piles,h):
                res.append(m)
                r = m - 1
            else:
                l = m + 1
        return min(res)
