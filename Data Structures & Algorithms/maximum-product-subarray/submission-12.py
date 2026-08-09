class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # with _product_ you need to 2 local optima, max and min -- because either could lead you to result 
        cur_max, cur_min, res = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            # we have to do this in-line, because we would have needed a temp variable. 
            cur_max, cur_min = max(num, num * cur_max, cur_min * num), min(num, cur_min * num, cur_max * num) # notice how the previous cur_max is not an option, we either have to extend this or ditch it and use num
            res = max(res, cur_max)
        
        return res