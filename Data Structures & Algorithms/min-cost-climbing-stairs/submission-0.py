class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # want min cost to reach top of the staircase --> store min for each step? (dp[])
        # can either move 1 step or 2.   

        # dp[n] = 0

        n = len(cost)

        dp = [-1] * (n + 1) # the min cost to reach the top (index n) from each position of the staircase

        dp[n] = 0
        dp[n-1] = cost[n-1]

        for i in range(n - 2, -1, -1):
            print("checking ", cost[i])
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
            print("dp[",i,"] = ", cost[i], " + ", min(dp[i + 1], dp[i + 2] ))

        return min(dp[0], dp[1])
