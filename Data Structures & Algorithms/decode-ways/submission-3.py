class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s) : 1} # number of ways to decode empty suffix will be 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 # 0 ways to decode 0, we will handle 2-digit numbers below 
            else:
                dp[i] = dp[i + 1] # if it's not 0, we know there's at least 1 way to decode it. 

            # handling 2-digit numbers: 
            # only add the one two away if this set of two numbers is 1-26
            # be careful not to allow 29
            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        
        return dp[0]