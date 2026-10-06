class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False # can't partition an odd sum array into two equal sum halves
        target = total // 2

        # now the question is can we partition the array into a subset which sums to target
        # can't use a 2-pointer or sliding window approach because the subset can be non-contiguous

        # decision at each index is to either include or exclude nums[i]
        # kind of a simple backtracking problem, but I think there's probably a DP optimization 

        dp = {} # (i, curSum) -> T/F
        def backtrack(i, curSum):
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
        

            