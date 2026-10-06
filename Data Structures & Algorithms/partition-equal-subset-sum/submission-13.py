class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False # can't partition an odd sum array into two equal sum halves
        target = total // 2

        #   0 1 2 3  (i)
        # 0 T T T T
        # 1   T F F
        # 2
        # 3
        # 4
        # 5.

        dp = {} # (i, curSum) -> T/F
        # using nums[i:], and current sum curSum, can we get to target?

        # now what if we flip it to using nums[i:] can we reach targetSum j?
        def backtrack(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            if curSum == target:
                dp[(i, curSum)] = True
            elif i == len(nums):
                dp[(i, curSum)] = False
            else:
                dp[(i, curSum)] = (
                    backtrack(i + 1, curSum + nums[i]) or 
                    backtrack(i + 1, curSum)
                )
            return dp[(i, curSum)]

        return backtrack(0, 0)
        # return dp[0][target]
        

            