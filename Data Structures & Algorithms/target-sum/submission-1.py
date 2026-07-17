class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        # decision tree: 
        # - add this number 
        # - subtract this number 

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1 # (we've gone through 0 elements, our current sum is 0) -> there is 1 way to get there. 

        for i in range(len(nums)):
            for prev_sum, prev_count in dp[i].items(): 
                # after going through i + 1 elements
                dp[i + 1][prev_sum + nums[i]] += prev_count 
                dp[i + 1][prev_sum - nums[i]] += prev_count 
        
        return dp[len(nums)][target]


