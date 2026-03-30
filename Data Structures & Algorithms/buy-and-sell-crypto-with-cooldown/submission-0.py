class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {} # key=(i, buying boolean) val=max_profit 

        def dfs(i, buying):
            if i >= len(prices):
                return 0 # out of bounds of prices[]
            if (i, buying) in dp:
                return dp[(i, buying)] # already calculated the max_profit for this
            
            cooldown = dfs(i+1, buying) # profit unchanged
            if buying:
                buy = dfs(i+1, not buying) - prices[i] # we just bought so less profit
                dp[(i, buying)] = max(buy, cooldown) # cache the max
            else:
                sell = dfs(i+2, not buying) + prices[i] # we just sold so more profit, also HAVE to take cooldown
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)


            


