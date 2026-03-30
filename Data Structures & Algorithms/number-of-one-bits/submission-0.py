class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0 
        while n > 0:
            # if rightmost bit is a 1
            if n & 1 == 1:
                count += 1
            n = n >> 1 # right shift
        
        return count