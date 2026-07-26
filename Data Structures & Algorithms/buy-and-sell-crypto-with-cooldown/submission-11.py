class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # dp[i][j] represents the max value on day i if you are looking to buy(j=0) or sell(j=1)

        # if you are looking to buy: j = 0
        #   - can either buy (switches you to looking to sell)
        #   - or skip 

        # if you are looking to sell: j = 1
        #   - you can either sell (and then must skip 1 day for cooldown)
        #   - or skip 


        # dp = [[0] * 2 for _ in range(len(prices) + 2)]
        next_1 = [0] * 2
        next_2 = [0] * 2

        for i in range(len(prices) - 1, -1, -1):
            today = [0] * 2
            for j in range(1, -1, -1):
                if j == 1: # selling
                    today[j] = max(
                        next_2[0] + prices[i], # sell and get price and skip day
                        next_1[1] # remain selling and skip day
                    ) 
                else: # j == 0 -> buying
                    today[j] = max(
                        next_1[1] - prices[i], # buy, switch back to selling
                        next_1[0] # skip, stay in selling
                    )
            next_2 = next_1
            next_1 = today

                

        return next_1[0]