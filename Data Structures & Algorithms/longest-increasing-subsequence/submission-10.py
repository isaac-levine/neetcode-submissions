from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[k] = the smallest value that can end an increasing subsequence of length k + 1
        # considering nums seen so far
        tails = [nums[0]] 

        for num in nums[1:]:
            if tails[-1] < num: # case 1: num is bigger than everything 
                tails.append(num)
            else:
                i = bisect_left(tails, num)
                tails[i] = num

        return len(tails)