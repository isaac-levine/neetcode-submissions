class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        best_buy = prices[0]

        if len(prices) == 1:
            return 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - best_buy) 
            best_buy = min(best_buy, prices[i])

        return max_profit
