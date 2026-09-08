class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # its not contiguous so its not a 2 pointer thing 
        # dp[i] = length of longest increasing subsequence ending at nums[i]

        dp = [1] * len(nums)
        for r in range(1, len(nums)):
            for l in range(r):
                if nums[l] < nums[r]:
                    dp[r] = max(dp[r], dp[l] + 1)
        return max(dp)