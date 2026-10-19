class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        # since we don't have to use each coin, I'm thinking that this is more likely to be able to use bottom up
        # and I'm seeing in the constraints that we don't have a lot of coins coins really don't go to that hyper value and amount stays pretty low 

        # so off the bat I'm thinking about some type of 2-D dynamic programming array where we have like the coins index in the amount and then I just wanna know using these certain subset of coins. Can I make this amount? 

        # so if I were to set this up as a DFS I would have an index I in an amount a and dfs(i, a) = num of ways to make a using coins[:i]

        # dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        for c in range(len(coins) + 1):
            dp[0][c] = 1

        for a in range(1, amount + 1): # skip 0, it's always 1.
            for c in range(len(coins) -1, -1, -1):
                coin = coins[c]
                dp[a][c] += dp[a][c + 1] # skip this coin. (reach to the right)
                if a >= coin:
                    dp[a][c] += dp[a - coin][c] # use this coin.. (reach up )

        return dp[amount][0]