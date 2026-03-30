class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        maxSum, curSum = nums[0], 0

        for n in nums:
            curSum = max(curSum, 0) + n
            maxSum = max(curSum, maxSum)

        return maxSum
        