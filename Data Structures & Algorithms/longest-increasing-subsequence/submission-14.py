from bisect import bisect_left # bisect_left(list, n) gives you leftmost index where n could be inserted while keeping the list in sorted order...
# leftmost element >= num
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[k] = the smallest value that can end an IS of length (k + 1)
        # considering nums seen so far
        # think of it as the "lowest bar for each length"
        tails = [nums[0]] 

        # [9,1,4,2,3,3,7]
        #              ^ 
        # tails = [1,2,3,7]

        for num in nums[1:]:
            # case 1: num is bigger than everything 
            if num > tails[-1]: 
                tails.append(num)
            else:
                # case 2: find the first point in tails to the left that is >= num
                i = bisect_left(tails, num)
                # at this point you know:
                # 1. everything to the left of i is < num
                # 2. tails[i] >= num
                tails[i] = num # so you should update it because num might be lower
                # because now we know that length i + 1 is achievable ending as low as i
        
        print("tails: ", tails)
        return len(tails)