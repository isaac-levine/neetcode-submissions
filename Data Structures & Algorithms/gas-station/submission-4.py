class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)

        # do you kind of just "kadane's" the diff array?

        tank = 0
        startingPoint = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0 # reset tank back to empty
                startingPoint = i + 1 # reset starting point to next index

        return startingPoint
        