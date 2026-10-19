class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums) + 1)] # second dimension (total) is a dict because the total can go negative....so can't use array index...
        # dp[i][total] = number of ways to reach `total` using the FIRST i numbers (nums[:i])

        # layer i is a finished world where i numbers have been consumed...


        dp[0][0] = 1 # total 0 is reachable using nothing. 

        for i in range(len(nums)):
            for total, numWays in dp[i].items(): # dp[i] = dict of key,val items {total : numWays}
                # push DP reads from the settled state and pushes the decision to the next
                dp[i + 1][total + nums[i]] += numWays
                dp[i + 1][total - nums[i]] += numWays

        
        return dp[len(nums)][target]


