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
        
        n = len(nums)
        pre, post, res = [0] * n, [0] * n, [0] * n 

        pre[0] = nums[0]
        post[n - 1] = nums[n - 1]

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]

        for i in range(n - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]

        res[0] = post[1]
        res[n - 1] = pre[n - 2]

        for i in range(1, n - 1):
            res[i] = pre[i - 1] * post[i + 1]

        return res
