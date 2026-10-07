class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # just did this recently. so i remember a lot of the mechanics
        # flip the problem...what if we burst this one last 
        # its interval dp 

        dp = {} 
        n = len(nums)
        nums = [1] + nums + [1]

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0
            
            windowBest = 0
            for i in range(l, r + 1):
                iMiddleGain = nums[l - 1] * nums[i] * nums[r + 1]
                windowBest = max(windowBest, iMiddleGain + dfs(l, i - 1) + dfs(i + 1, r))
            dp[(l, r)] = windowBest
            return windowBest


        return dfs(1, n)