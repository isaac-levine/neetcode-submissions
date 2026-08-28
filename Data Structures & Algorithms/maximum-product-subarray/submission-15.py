class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin = curMax = res = nums[0]

        for num in nums[1:]:
            curMin, curMax = min(num, 0, curMax * num, curMin * num), max(num, 0, curMax * num, curMin * num)
            res = max(res, curMax)
            
        
        return res
