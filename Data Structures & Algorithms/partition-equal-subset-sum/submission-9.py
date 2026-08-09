class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False # can't work with an odd sum
        
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True # sum 0 is always achievable.
        # dp[i] = can we form sum i using nums[:i+1]

        for num in nums:
            # for each sum s between target and num
            for s in range(target, num - 1, -1):
                dp[s] |= dp[s - num]

        
        return dp[target]