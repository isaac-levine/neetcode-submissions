class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # 1, [4,2,3,7], 1

        # recursive decision: which ballon do i want to pop LAST? -- because that's an irreversible decision. if i pop it last its last

        # subproblem becomes what is the maximum number of coins for subinterval [l, r] and you know what it is for sure. 

        # what to remember / state: the balloons that you had to choose from and where you decided to pop? 
        # 

        # for each candidate number to pop last
            # 1 * candidate * 1
            # + dp(left subarray) = dp[i + 1][r]
            # + dp(right subarray) = dp[l][i - 1]

        # time complexity is O(n^3) because there are O(n^2) number of subarrays and for every subarray we have to iterate through every value 

        nums = [1] + nums + [1]
        dp = {} 

        def dfs(l, r) -> int:
            if l > r:
                return 0 # range has collapsed to nothing.
            if (l, r) in dp:
                return dp[(l, r)] # already computed and cached
            maxCoins = 0
            for i in range(l, r + 1): # try each position i as the LAST balloon to burst.
                # try popping this one last
                middle = nums[l - 1] * nums[i] * nums[r + 1]
                maxCoins = max(maxCoins, middle + dfs(i + 1, r) + dfs(l, i - 1))
            dp[(l, r)] = maxCoins
            return maxCoins 


        return dfs(1, len(nums) - 2)