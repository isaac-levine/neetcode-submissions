class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # if amount == 0:
        #     return 1

        # dp = [0] * (amount + 1)
        # dp[0] = 0 # "" are your coins, base case

        # decision: use/don't use the coin
        # state: what amount that decision gave us
        # recurrence relation: number of ways for this target is the number of ways to reach the one `coin` spots before this + what's already here. 
        # dp[target] += dp[target - coin] if coin <= target else 0 

        # dp[i][j] = number of distinct ways to make amount i with coins[j:]

        #     1 2 3
        #    ________
        # 0 | 1 1 1 0 
        # 1 | 1 0 0 0
        # 2 | 2 1 0 0
        # 3 | 3 1 1 0
        # 4 | 4 1 0 0

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

        