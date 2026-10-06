class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False # can't partition an odd sum array into two equal sum halves
        target = total // 2

        #.  0 1 2 3 4 5 
        # 1 T T F F F F
        # 2 T   T T F F 
        # 3 T     T T T
        # 4 T       T T 

        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for s in range(target, num - 1, -1): # its start stop step not start step stop
                dp[s] = dp[s] or dp[s - num]
        
        return dp[target]