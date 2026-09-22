class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2

        # basically can partition in such a way that we get to target sum 
        # backtracking 

        def backtrack(i, cur):
            if cur == target:
                return True
            elif i == len(nums):
                return False
            
            return backtrack(i + 1, cur + nums[i]) or backtrack(i + 1, cur)
        
        return backtrack(0, 0)
