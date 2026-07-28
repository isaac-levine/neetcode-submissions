class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1 # "goal" = the position you must be able to reach to say you can jump to the end 

        for i in range(len(nums) - 1, -1, -1):
            if (i + nums[i]) >= goal:
                goal = i
        
        return goal == 0