class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        buy_1_away, buy_2_away, sell_1_away = 0, 0, 0
        for i in range(N - 1, -1, -1):
            # either buy it today and enter selling state tomorrow, or stay in buying state 
            buying_today = max(sell_1_away - prices[i], buy_1_away) 
            # either sell it today and enter buying state tomorrow, or stay in selling state
            selling_today = max(buy_2_away + prices[i], sell_1_away)

            buy_2_away = buy_1_away
            buy_1_away = buying_today
            sell_1_away = selling_today

        return buy_1_away
