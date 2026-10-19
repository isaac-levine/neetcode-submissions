class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int) # second dimension (total) is a dict because the total can go negative....so can't use array index...
        # dp[i][total] = number of ways to reach `total` using the FIRST i numbers (nums[:i])

        # layer i is a finished world where i numbers have been consumed...

        dp[0] = 1 # total 0 is reachable using nothing. 


        for num in nums:
            nextDp = defaultdict(int)
            for total, numWays in dp.items(): # dp[i] = dict of key,val items {total : numWays}
                # push DP reads from the settled state and pushes where the decision lands....
                # settled state is dp[i].items()...{total : numWays} using nums[:i] (does not include index i...)
                
                # so now that we ARE using index i... we can push to dp[i + 1]
                nextDp[total + num] += numWays
                nextDp[total - num] += numWays
            
            dp = nextDp

        
        return dp[target] # does not include index len(nums) obviously...because that's out of bounds