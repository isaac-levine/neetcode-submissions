class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False # can't work with an odd sum
        
        target = sum(nums) // 2
        

        # decision tree
        # either include this in my sum, or don't include it in my sum. if i can reach target, it's true. 

        # [1,2,3,4]
        # 

        def backtrack(i, curSum):
            if i >= len(nums) or curSum > target:
                return False
            if curSum == target:
                return True

            # use it or don't use it. 
            return backtrack(i + 1, curSum + nums[i]) or backtrack(i + 1, curSum)

        return backtrack(0, 0)