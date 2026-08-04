class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        wall = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= wall:
                wall = i
        
        return wall == 0