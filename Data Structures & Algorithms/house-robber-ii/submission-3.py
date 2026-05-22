class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def og(nums: List[int]) -> int:
            close, far = 0, 0
            for num in nums:
                cur = max(far + num, close)
                far = close
                close = cur
            return close


        if len(nums) == 1:
            return nums[0]
        return max(og(nums[1:]), og(nums[:len(nums) - 1]))

