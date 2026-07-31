class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        # for each coin, can choose to skip it (move to i + 1), or use it and stay here (i)


        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        #   0 1 2 3 4   amounts
        # 0 1
        # 1 1
        # 2 1
        # 3 1 0 0 0 0 

        for r in range(len(coins) + 1):
            dp[r][0] = 1

        # coin indexes

        # dp[c][a] = how many ways can you make amount a with coins[c:]
        # leftmost column represents how many ways can you make amount 0 with coins[c:]
        for c in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[c][a] += dp[c + 1][a] # skip this coin
                # use this coin if its less than amount
                if c <= amount:
                    dp[c][a] += dp[c][a - coins[c]] # stay on this coin, but new target amount is amount - value of the coin.

        return dp[0][amount]
