class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Off bat I know this is something knapsack but I'm not really sure I even remember what that means to me lol 

        # return total number of distinct combinations that total up to amount 
        # else return 0 

        # unlimited number of each coin and each value in coins is unique 

        # its a knapsack because we're taking the coins and putting them into our little sack like a clash of clans goblin

        #                0...amount
        # 0
        # .
        # . 
        # .
        # len(coins) - 1

        # dp[i][j] can I make amount j with coins[i:]

        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(amount + 1):
                if c <= a:
                    dp[a] += dp[a - c] 

                # can either use it or skip it 
                # using it means amount - coin

                # skipping it means going to the previous value 
                # so you just add them 

                # but if we just reuse one dp array then the previous value is already sitting there in our lap
        
        
        return dp[amount]

