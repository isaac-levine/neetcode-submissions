class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [float("inf")] * (amount + 1) # dp[i] = fewest number of coins needed to make target amount i.
        dp[0] = 0

        for t in range(1, amount + 1):
            # can we make target t with the coins? 
            for c in coins:
                if c == t:
                    dp[t] = 1
                    break # does this break the for loop? 
                if t >= c and dp[t - c] != float("inf"):
                    dp[t] = min(dp[t - c] + 1, dp[t])

        return dp[amount] if dp[amount] != float("inf") else -1 