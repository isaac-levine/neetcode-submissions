class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1 

        # because of the check above, we know a solution exists? 

        total = 0 
        res = 0 
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            # every time a starting position doesn't work, we're going to be
            # greedy and reset it back to 0 
            if total < 0:
                total = 0
                res = i + 1
        
        return res