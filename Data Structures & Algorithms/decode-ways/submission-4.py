class Solution:
    def numDecodings(self, s: str) -> int:
        
        # at each position, you're deciding to take one digit or take 2. 
        # valid 2-digit codes are 10-26
        # each dp[i] represents number of ways to decode the string starting at position i. 


        one_ahead, two_ahead, cur = 1, 0, 0 # 1 way to decode "", other variable is just garbage to start (unused until pos i - 2)
        for i in range(len(s) - 1, -1, -1):

            # case where we take 1 digit
            if s[i] != "0":
                cur += one_ahead # taking one digit doesn't add a new way, it inherits the ways of one_ahead


            # case where we take 2 digits. 
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cur += two_ahead

            cur, one_ahead, two_ahead = 0, cur, one_ahead

        
        return one_ahead


