class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        dp = {} 
        a = [1] + nums + [1]

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0
            
            windowBest = 0
            for i in range(l, r + 1):
                iMiddleGain = a[l - 1] * a[i] * a[r + 1]
                windowBest = max(windowBest, iMiddleGain + dfs(l, i - 1) + dfs(i + 1, r))
            dp[(l, r)] = windowBest
            return windowBest

        return dfs(1, len(a) - 2)