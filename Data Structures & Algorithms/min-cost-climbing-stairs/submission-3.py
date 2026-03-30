class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # want min cost to reach top of the staircase --> store min for each step? (dp[])
        # can either move 1 step or 2.   

        # dp[n] = 0

        n = len(cost)

        # dp = [-1] * (n + 1) # the min cost to reach the top (index n) from each position of the staircase

        big = 0
        little = cost[n - 1]
        cur = -1 

        for i in range(n - 2, -1, -1):
            cur = cost[i] + min(big, little)
            big = little
            little = cur 

            # dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(big, little)
