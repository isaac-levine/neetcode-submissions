class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def house_robber(nums: List[int]) -> int: 
            far, close = 0, 0 

            for num in nums:
                cur = max(far + num, close)
                far = close
                close = cur
            
            return close
        
        return max(house_robber(nums[1:]), house_robber(nums[:len(nums) - 1]), nums[0])
