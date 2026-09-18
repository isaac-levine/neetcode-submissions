from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # tails represents the "lowest bar for each LIS length", 
        # so tails[k] = the smallest value that can end an LIS of length k 

        tails = [nums[0]]

        for n in nums[1:]:
            # case 1: this num is bigger than the bar for ending the longest LIS available. 
            if n > tails[-1]:
                tails.append(n) 
            else:
                i = bisect_left(tails, n) # gives us the leftmost element that is still >= n
                tails[i] = n
        
        return len(tails)
