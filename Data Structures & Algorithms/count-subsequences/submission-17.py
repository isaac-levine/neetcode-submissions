class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        # off bat: not contiguous substrings so definitely not two pointer or anything standard like that...
        # i think its two sequence 2d dp where we align both sequences as axes on our 2d dp [][]

        # dp[i][j] = number of distinct subsequences of s[i:] which are equal to t[j:]

        #    c  a  t
        # c  3  3  1  1
        # a  0  3  1  1
        # a  0  2  1  1
        # a  0  1  1  1
        # t  0  0  1. 1
        #             1        < -- and then I think we fill the bottom row with 0's because the only way to make something with "" is if you're trying to make "'" ( bottom right corner.)
        #.            ^ always one way to make empty string, it's ""
        # but actually we only need to pre-fill a 1 in this very bottom right corner because we never read directly to our right
        # wait actually scratch that I think we need it so we can read it because we wont recurse and fill it as we go backwards 

        # choice at each position: you can either skip this character or use it. 
        # skip: add the one below
        # use: add the one to diagonal ( + 1, + 1) iff the current characters match in both strings

        # so at each position we're adding the one below and then if the characters match, also the one diagonal (down, right)

        # let's just walk through this quickly with one more example...


        #   x y
        # x 5 2 1
        # x 3 2 1
        # y 1 2 1
        # x 1 1 1
        # y 0 1 1
        #       1
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)] # i think the rows go on the more outer thing...
        for r in range(m + 1):
            dp[r][n] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] += dp[r + 1][c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1]



        return dp[0][0]

