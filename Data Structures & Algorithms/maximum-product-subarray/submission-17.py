class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin = curMax = res = nums[0]

        for num in nums[1:]:
            prevMin = curMin
            curMin = min(num, curMax * num, curMin * num)
            curMax = max(num, curMax * num, prevMin * num)
            res = max(res, curMax)
        return res
