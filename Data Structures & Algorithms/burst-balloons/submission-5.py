class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        

        # off bat I remember this one having some weird mechanics to it where its kind of reaching outside of its own window recursively to work 
        # and then I think we can do some trick to pad the array or something like that....

        # and overall I think its interval DP...
        # where dp[(l, r)] = the max you can get over window [l, r]

        # oh and iirc we want to flip the problem somehow, so for the window we iterate over each position i and ask what if we pop i LAST?
        # that means you just add nums[i] to the end. 

        # that way you are able to concretely recurse on a window either to the left or to the right of that i.... and then you just combine the results together after they return. 

        # ok so for all dp problems i know there are some questions we need to ask ourselves
        # what do i need to remember about each subproblem? --> just the window and what the maximimum number of coins / balloons was....

        # what is the recurrence relation...well its the max of nums[i] + 2 windows where nums[i] is each position in the given window.... so its kind of an n-ary backtracking problem 



        n = len(nums)
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            elif l > r:
                return 0 

            windowMax = 0
            for i in range(l, r + 1):
                cur = (nums[l - 1] * nums[i] * nums[r + 1])
                windowMax = max(windowMax, cur + dfs(l, i - 1) + dfs(i + 1, r))
            
            dp[(l, r)] = windowMax
            return dp[(l, r)]
        

        return dfs(1, n)



