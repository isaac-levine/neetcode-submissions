class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # dp, kind of just from memory of the problem 
        # interval DP specifically where you have like the left and right pointers and that defines your cache? 

        # now i remember we want to FLIP the problem and consider what if I pop this balloon LAST in this window.
        # pick an i to be LAST -- then you just recurse on the two sides with new calls....

        # input - nums is small and values in nums are small as well...seems like we can do something brute forcey...

        # artificially pad the input array
        nums = [1] + nums + [1]

        dp = {} # (l, r) : maxCoins for that window 

        def dfs(l, r):
            if l > r:
                return 0 
            elif (l, r) in dp:
                return dp[(l, r)]

            windowBest = 0
            for i in range(l, r + 1):
                # take this one last.
                # but then how do we make sure we're maximizing the top-level result and not the smallest subproblem 
                iLast = nums[l - 1] * nums[i] * nums[r + 1] # This and the padding is the part that I tripped up on for sure this time and last time
                # in other words, the way this subproblem kind of reaches beyond its constraints and communicates with the rest of the nums array. very tricky to me
                windowBest = max(windowBest, iLast + dfs(l, i - 1) + dfs(i + 1, r))
            dp[(l, r)] = windowBest
            return windowBest

        return dfs(1, len(nums) - 2)


