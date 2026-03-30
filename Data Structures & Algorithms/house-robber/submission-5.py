class Solution:
    def rob(self, nums: List[int]) -> int:
        
        far, close = 0, 0
        
        for num in nums:
            cur = max(far + num, close)
            far = close
            close = cur
        
        return close 
