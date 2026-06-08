class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            minCoins = float("inf")
            for c in coins:
                if (amt - c) >= 0 and dp[amt - c] != float("inf"):
                    minCoins = min(minCoins, 1 + dp[amt - c])

            dp[amt] = minCoins 

    
        return dp[amount] if dp[amount] != float("inf") else -1
