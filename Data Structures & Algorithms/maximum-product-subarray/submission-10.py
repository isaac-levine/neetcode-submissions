class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # with _product_ you need to 2 local optima, max and min -- because either could lead you to result 
        cur_max, cur_min, res = nums[0], nums[0], nums[0]

        # [2,4,-3,5]
        # cur_max = 8
        # cur_min = 2
        # res = 2

        for num in nums[1:]:
            cur_max, cur_min = max(num, num * cur_max, cur_min * num), min(num, cur_min * num, cur_max * num) # notice how the previous cur_max is not an option, we either have to extend this or ditch it and use num
            res = max(res, cur_max)
        
        return res