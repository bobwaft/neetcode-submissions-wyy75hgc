class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        targ = stoneSum//2
        dp = [0]*(targ+1)
        for stone in stones:
            for i in range(targ,stone-1,-1):
                exclude = dp[i]
                include = stone + dp[i-stone]
                dp[i] = max(exclude,include)
        return stoneSum- 2*dp[targ]