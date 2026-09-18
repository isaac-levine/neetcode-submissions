class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # off bat: the subsequence might not be contiguous, so can't do 2 pointers or sliding window
        # nums are small and len(nums) is also small... so thinking maybe we can do something inefficient

        # maybe dp[i] = length of LIS ending with nums[i]
        # so for nums = [9,1,4,2,3,3,7]
        #         dp  =  1,1,2,2,3,3,4

        # nums = [0,3,1,3,2,3]
        #   dp =. 1,2,2,3,3,4

        dp = [1] * len(nums)

        for i in range(len(nums)):
            num = nums[i]
            longestLessThanNum = 0
            
            for j in range(i):
                if nums[j] < num:
                    longestLessThanNum = max(longestLessThanNum, dp[j])
            
            dp[i] = 1 + longestLessThanNum

        return max(dp) 
        