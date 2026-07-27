class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        N = len(nums)

        dp = [False] * N
        dp[N - 1] = True

        for i in range(N - 2, -1, -1):
            for j in range(nums[i], 0, -1):
                if (i + j) < N and dp[i + j]:
                    dp[i] = True
        
        return dp[0]
