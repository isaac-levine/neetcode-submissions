class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # This is a similar approach to Partition Equal Subset Sum.
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if ((a - c) >= 0 and dp[a - c] != float("inf")):
                    dp[a] = min(dp[a], 1 + dp[a - c])


        return dp[amount] if dp[amount] < float("inf") else -1

