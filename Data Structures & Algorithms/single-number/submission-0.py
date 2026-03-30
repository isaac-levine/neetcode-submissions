class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # return the integer in nums that appears only once
        # O(n) time and O(1) space

        res = 0
        for num in nums:
            res ^= num 
        return res