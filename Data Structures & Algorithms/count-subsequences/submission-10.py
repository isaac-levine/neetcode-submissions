class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # def dfs(i, j)

        # What is my recursive decision? --> Use or skip this s[i]
        # What do I need to remember about those decisions? --> i and j, where i is position in s and j is position in t
        # This is probably a pull, because we know at the end of the array is a base case that we can build off. 
        # What are my base cases? --> There 
        # What is the reccurence? --> num ways when you skip + num ways when you use it. 
        #                           = dfs(i + 1, j) (skip it) + dfs(i + 1, j + 1) (use it)

        dp = [0] * (len(t) + 1)

        dp[len(t)] = 1 # there is exactly 1 way to build "", no matter what you have. you just skip everything. 

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)):
                
                # dp[j] += dp[j] # skip this s[i] <--- this is automatically taken care of. dp[j] starts out as the prev[j]
                # or use this s[i] if the character's match
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]

        
        return dp[0]

