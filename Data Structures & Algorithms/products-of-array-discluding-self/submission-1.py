# Products of Array Except Self
# Solved 
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# 
# Each product is guaranteed to fit in a 32-bit integer.
# 
# Follow-up: Could you solve it in 
# O(n) time without using the division operation?
# 
# Example 1:
# 
# Input: nums = [1,2,4,6]
# 
# Output: [48,24,12,8]
# Example 2:
# 
# Input: nums = [-1,0,1,2,3]
# 
# Output: [0,-6,0,0,0]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [0] * len(nums)
        backward = [0] * len(nums)
        # more memory way 
        forward[0] = nums[0]
        backward[len(nums) - 1] = nums[len(nums) - 1]

        
        # forward represents the increasing product going ---> so it represents the product of myself and everything that came BEFORE me  
        # backward represents the increasing product going <--- 

        # the result will be the product of forward[i-1] * backward[i + 1] 
        
        # build forward 
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] * nums[i]

        print("forward: ", forward)

        # build backward
        for i in range(len(nums) - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i]  

        print("backward: ", backward)

        # build the result array
        res = [0] * len(nums)
        res[0] = backward[1]
        for i in range(1, len(nums) - 1):
            res[i] = forward[i - 1] * backward[i + 1]


        res[len(nums) - 1] = forward[len(nums) - 2]


        return res
