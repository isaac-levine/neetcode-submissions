class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int) # targetSum -> numWays
        dp[0] = 1

        for num in nums:
            # push out into unknown space the next layer of dp....
            nextDp = defaultdict(int)
            for total, count in dp.items():
                nextDp[total + num] += count
                nextDp[total - num] += count
            dp = nextDp
        return dp[target]