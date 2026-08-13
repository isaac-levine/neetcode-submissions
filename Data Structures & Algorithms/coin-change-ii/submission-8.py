class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        #   0 1 2 3 4   (amount)
        # 1 1 1 2 3 4 0  # <--- reach to the left to find dp[amount - coin] (use this )
        # 2 1 0 1 1 1 0  # <--- reaech down to find skip
        # 3 1 0 0 1 0 0

        # use it and add it to dp[amt-coin], or skip it and add it to one to the right 
        # if coin matches amount += 1

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coinIdx in range(len(coins) - 1, -1, -1):
            for target in range(amount + 1):
                coin = coins[coinIdx]
                if coin <= target:
                    dp[target] += dp[target - coin] # by the nature of how we're moving through the 2d space, this will be what was left from the row before us, so we don't need to do the other += case...

        
        return dp[amount]

        