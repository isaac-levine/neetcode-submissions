class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

#         # decision tree: 
#         # - you can skip this coin (move to position i + 1)
#         # - or you can use this coin (a + coins[i], and because there's unlimited, you have to stat at position i)

#         # dp[c][a] = number of distinct combinations to get to amount, using coins from coins[c] onward through the end 
#         dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
#         for i in range(len(coins) + 1):
#             dp[i][0] = 1 # set the whole leftmost column to 1 because there is always 1 way to make amount 0. 
        
# # amount: 0 1 2 3
# #       ---------- 
#         # 1 0 0 0 |  using coin 0 onward
#         # 1 0 0 0 |  using coin 1 onward
#         # 1 0 0 0 |  using coin 2 onward
#         # 1 0 0 0 |  using coin 3 onward 

#         for c in range(len(coins) - 1, -1, -1):
#             for a in range(1, amount + 1):
#                 dp[c][a] += dp[c + 1][a] # skip and go to the next coin
#                 if coins[c] <= a: # can we even use this coin? only if its smaller than amount we have left. 
#                     dp[c][a] += dp[c][a - coins[c]] # remember you have to stay if you decide to use this coin 

#         return dp[0][amount]

        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        
        return dp[amount]

