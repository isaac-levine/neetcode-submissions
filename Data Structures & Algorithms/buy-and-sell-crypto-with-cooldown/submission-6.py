class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        buy1, buy2, sell1 = 0, 0, 0
        for i in range(N - 1, -1, -1):
            buying_today = max(sell1 - prices[i], buy1) # either buy it today and enter selling state tomorrow, or stay in buying state 
            selling_today = max(buy2 + prices[i], sell1) # either sell it today and enter buying state tomorrow, or stay in selling state

            buy2 = buy1
            buy1 = buying_today
            sell1 = selling_today

        return buy1
