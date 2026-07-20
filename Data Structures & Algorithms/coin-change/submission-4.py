class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for coin in coins:
            curRow = [0] * (amount+1)
            for m in range(amount+1):
                exclude = dp[m]
                include = float("inf")
                if m - coin >= 0:
                    include = 1 + curRow[m-coin]
                curRow[m] = min(exclude,include)
            dp = curRow
        if curRow[m] == float("inf"):
            return -1
        return dp[m]