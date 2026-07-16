class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        # # each row represents one day. 
        # # and each row has 2 columns, representing the max for the buying state and the max for the selling state of that day.
        # #    [[buying, selling]]
        # dp = [[0, 0] for _ in range(N + 2)] # dp[i][0] -> max profit if we are in buying state
        #                                     # dp[i][1] -> max profit if we are in selling state
    
        # for i in range(N - 1, -1, -1):
            
        #     # if we are in "buying" state today. deciding to buy or hold 
        #     dp[i][0] = max(
        #         dp[i + 1][1] - prices[i], # buy: must be in selling state tomorrow
        #         dp[i + 1][0] # hold: maybe buy tomorrow  
        #     )

        #     # if we are in "selling" state today. deciding to sell or hold 
        #     dp[i][1] = max(
        #         dp[i + 2][0] + prices[i], # sell: must skip one day and then enter buying state
        #         dp[i + 1][1] # hold: maybe sell tomorrow
        #     )

        # return dp[0][0]

        buy1, buy2, sell1 = 0, 0, 0
        for i in range(N - 1, -1, -1):
            buying_today = max(sell1 - prices[i], buy1) # either buy it today and enter selling state tomorrow, or stay in buying state 
            selling_today = max(buy2 + prices[i], sell1) # either sell it today and enter buying state tomorrow, or stay in selling state

            buy2 = buy1
            buy1 = buying_today
            sell1 = selling_today

        return buy1
