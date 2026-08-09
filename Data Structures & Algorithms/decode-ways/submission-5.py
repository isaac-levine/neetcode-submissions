class Solution:
    def numDecodings(self, s: str) -> int:
        
        # 226
        # 22, 6
        # 2, 2, 6
        # 2, 26

        # 2 2 6 
        # 3 2 1 1

        # 1 2 2 6 <-- the 4 has to standalone 
        # 5 3 2 1 1 

        # 1 2 2 6
        # 1 22 6
        # 1 2 26
        # 12 26
        # 12 2 6

        # single digit case --> dp[i] = dp[i + 1]
        # two-digit case --> dp[i] += dp[i + 2]
        # skip a zero? 

        # 1 2 
        # 2 1 1

        dp = [0] * (len(s) + 1) # dp[i] = the number of ways to decode s[i:]
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            # 1. single digit case
            if s[i] in "123456789":
                dp[i] += dp[i + 1]
            
            # 2. two digit case
            #   2a. 1 and 0-9
            #   2b. 2 and 0-6
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]


        return dp[0]