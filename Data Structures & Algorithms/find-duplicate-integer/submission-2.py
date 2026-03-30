class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # the reason this is a LL problem, is because if you just do cycle detection that's an easy way to solve
        # constraint: do not modify nums, and use constant O(1) extra space 

        # nums = [-1,-2,-3,2,2]

        # take the index of the absolute value - 1 so 1 --> 0  and -1 --> 0 that means you found a duplicate 

        # [3,1,-3,4,2]

        for i, n in enumerate(nums):
            if nums[abs(n) - 1] < 0:
                return abs(n)
            nums[abs(n) - 1] *= -1

        return -1 
