class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        
        for num in nums:
            for subsetSum in range(target, num - 1, -1):
                dp[subsetSum] = dp[subsetSum] or dp[subsetSum - num]                
        

        return dp[target]