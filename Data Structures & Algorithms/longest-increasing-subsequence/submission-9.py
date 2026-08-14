class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # since subsequences are not contiguous -> it's not sliding window/2 pointer
        
        dp = [1] * len(nums)

        for r in range(1, len(nums)):
            for l in range(r):

                # found some continuation of a previous subsequence
                if nums[r] > nums[l]:
                    dp[r] = max(dp[r], dp[l] + 1)


        return max(dp)