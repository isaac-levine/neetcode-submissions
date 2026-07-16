class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # State: are we buying or selling? 
        # If Buy -> i + 1
        # If Sell -> i + 2

        # this is our cache 
        dp = {} # key = (i, buying). val = max_profit

        def dfs(i, buying):
            # base cases 
            if i >= len(prices): # out of bounds 
                return 0 
            if (i, buying) in dp: # in our cache 
                return dp[(i, buying)]

            # now the actual decision
            # depends on what "state" we're in (whether we are buying or selling right now)
            if buying:
                # can either buy or cooldown
                buy = dfs(i + 1, not buying) - prices[i] # if we buy, we have to subtract current price 
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown) # cache the higher profit for this position and state
            else:
                # can either sell or cooldown
                sell = dfs(i + 2, not buying) + prices[i] # remember i + 2 because after you sell you have to take a cooldown day 
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)