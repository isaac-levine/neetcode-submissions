from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[k] = the smallest value that can end an increasing subsequence of length k + 1
        # considering nums seen so far
        tails = [nums[0]] 

        for num in nums[1:]:
            if num > tails[-1]: # case 1: num is bigger than everything 
                tails.append(num)
            else:
                # case 2: find the first point in tails to the left that is <= num
                tails[bisect_left(tails, num)] = num

        return len(tails)