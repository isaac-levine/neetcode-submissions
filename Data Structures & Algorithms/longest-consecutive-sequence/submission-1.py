class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
        if len(nums) == 0:
            return 0 

        numSet = set(nums) 
        longest = 1 
        
        for n in nums:
            # is it the start of a sequence? 
            if (n - 1) not in numSet:
                # yes
                cur = 0  
                while n in numSet:
                    cur += 1
                    n += 1
                longest = max(longest, cur) 


        return longest 
