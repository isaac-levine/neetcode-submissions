class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        N = len(cost)
        minCost = [float("inf")] * N

        minCost[0] = cost[0]
        minCost[1] = cost[1]

        for i in range(2, N):
            minCost[i] = cost[i] + min(minCost[i - 1], minCost[i - 2])


        return min(minCost[N - 1], minCost[N - 2])

