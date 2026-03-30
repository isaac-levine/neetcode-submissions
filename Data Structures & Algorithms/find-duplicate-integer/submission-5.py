class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        # given: all numbers are positive
        # rule: if nums[i] is negative, we've already seen i 

        # [1,2,3,2,2]
        # [1,2,3,4,4]


        for n in nums:
            if nums[abs(n)] < 0:
                return abs(n) 
            nums[abs(n)] = -1 * nums[abs(n)]

        return -1 
