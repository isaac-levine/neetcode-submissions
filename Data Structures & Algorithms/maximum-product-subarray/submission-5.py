class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        res = curMax = curMin = nums[0]
        for n in nums[1:]:
            curMax, curMin = max(n, curMax * n, curMin * n), min(n, curMax * n, curMin * n)
            res = max(res, curMax, curMin)
        
        return res
