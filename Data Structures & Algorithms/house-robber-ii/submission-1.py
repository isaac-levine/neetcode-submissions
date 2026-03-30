class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_og(arr: List[int]) -> int:
            far, close = 0, 0
            for num in arr:
                cur = max(far + num, close)
                far = close
                close = cur
            return close 
        
        return max(rob_og(nums[1:]), rob_og(nums[:len(nums)-1]))

                

