class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        
        # we know an answer exists now 
        diff = [gas[i] - cost[i] for i in range(n)]

        # do you kind of just "kadane's" the diff array?

        tank = 0
        start = 0
        for i in range(n):
            tank += diff[i]
            if tank < 0:
                tank = 0 # reset tank back to empty
                start = i + 1 # reset starting point to next index

        return start
        