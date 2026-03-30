class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums=[4,5,6]
        # target=10

        numToIndex = {} 

        for i in range(len(nums)): 
            n = nums[i]

            # already seen this number's complement 
            if (target - n) in numToIndex:
                return [numToIndex[target - n], i]
            else:
                numToIndex[n] = i


