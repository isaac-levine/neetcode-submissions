class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        # what is the thing to memoize? 
        # the maximum product if you use this number?   

        cur_min, cur_max, res = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            cur_max, cur_min = max(num, cur_min * num, cur_max * num), min(num, cur_min * num, cur_max * num)
            res = max(res, cur_max)
        
        return res