class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # dp[i][total] = the number of ways using nums[:i] to reach that total. 
        # this total can spread outwards in either positive or negative direction
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # all you need is the leftmost single node to start, and then you do build each next layer (size doubles every time)
        # right before walking it, and then building the next layer again...
        # then at the end, you just return dp[len(nums)][target]
        dp[0][0] = 1 # there is 1 way to reach nothing with nothing

        # if we did dfs this... it would be def dfs(i, curTotal): 
        # dp[i, curTotal] = # of ways to reach cur total with nums up to i 

        for i in range(len(nums)):
            # build the next layer right before you walk it 
            # for each total achievable by the first i numbers 
            for total, count in dp[i].items():
                # the first i + 1 numbers for (total + nums[i]) gets extended by this count
                dp[i + 1][total + nums[i]] += count # there are 'count' more ways to reach (total+nums[i])  
                # the first i + 1 numbers for (total - nums[i]) gets extended by this count
                dp[i + 1][total - nums[i]] += count 


        return dp[len(nums)][target]
