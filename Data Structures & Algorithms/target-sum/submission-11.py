class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # I think dp off the bat 
        # but wait its contiguous and you use every number in the array so maybe its greedy or something? 
        # or is it a push DP ? 

        # i think it might actually be a push DP yeah wher we go through all the sums that we just made from the last level 
        # and then we just check them at the end to see if target is in there? 

        # i mean nums is really small so I feel like this might actually be it...

        dp = defaultdict(int) # total -> numWays
        dp[0] = 1
        
        for n in nums:
            nextDp = defaultdict(int)
            for total, count in dp.items():
                nextDp[total + n] += count
                nextDp[total - n] += count
            dp = nextDp
            

        return dp[target]