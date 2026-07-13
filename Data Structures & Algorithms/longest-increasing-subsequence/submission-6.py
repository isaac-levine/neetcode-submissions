class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            longest = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    longest = max(longest, dp[j] + 1)
            dp[i] = longest

        return max(dp)