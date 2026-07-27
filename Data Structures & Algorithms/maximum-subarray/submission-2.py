class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # "find the subarray and..." is kind of misleading because all we care about is the actual sum, not the subarray itself

        res = nums[0] # what if all negative numbers? can't start with 0 
        cur = 0 

        for num in nums:
            cur = max(cur + num, num) # choice: extend contiguous subarray, or reset.
            res = max(res, cur)

        return res

        # [2,-3,4,-2,2,1,-1,4]
        # res = 8
        # cur = 8

        # [-1]
        # res = -1
        # cur = 0  