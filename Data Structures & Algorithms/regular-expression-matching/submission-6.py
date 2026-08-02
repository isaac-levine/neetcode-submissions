class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        # recursive decision: what to do with this pattern? --> character matches? or any character at all (.)? or some number 0 or more of whatever comes before the *??
        # state: position in s and p 
        # recurrence relation: whether or not the rest of the string can match....if we hit a *, let's keep going until we see what character we're dealing with?

        # do we want to push or pull? i feel like pushing could be easier, are we dependent on anything later on????
        # but actually i think pulling will allow us to space optimize....we just have to check what letter p[i-1] is if we see a star....

        #   . * z 
        # x       F
        # y       F
        # z     T F
        #.        T

        # we need to compute the bottom row, but not the rightmost column 

        # dp[i][j] = can s[i:] be made with pattern p[j:]

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        for r in range(len(s)):
            dp[r][len(p)] = False
        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # 1. if the two characters match or if p is . -> set it to the diagonal.. this is what we'll define as firstMatch

                # 2. if p is a star: the key that makes the code understandable is that we don't deal with a star, until we're one space to the left of it. so we don't have 
                # to deal with any messy skipping or anything like that 
                    # 2a: use this character 0 times --> move to the next character and next pattern thing.
                    # 2b: use this character at least 1 time. --> move to the next character but stay here on the pattern thing? 

                firstMatch = j < len(p) and i < len(s) and (s[i] == p[j] or p[j] == ".")

                # check for star FIRST 
                if j < len(p) - 1 and p[j + 1] == "*":
                    dp[i][j] = (
                        dp[i][j + 2] or # don't use the star at all.
                        (firstMatch and dp[i + 1][j]) # use it at least once: character needs to match but we can continue using it, so leave j in place.
                    )
                else:
                    # next in p is not a star, so we need either a regular match or a '.'
                    dp[i][j] = firstMatch and dp[i + 1][j + 1]

        return dp[0][0]