class Solution:
    def rob(self, nums: List[int]) -> int:
        
        far, close = 0, 0 

        for num in nums:
            cur = max(num + far, close)
            far = close
            close = cur
        
        return cur 