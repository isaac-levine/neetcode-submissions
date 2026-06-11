class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True

        for num in nums:
            for subsetSum in range(target, num - 1, -1): # process all subsetSums from target down to num inclusive
                dp[subsetSum] = dp[subsetSum] or dp[subsetSum - num]

        return dp[target]