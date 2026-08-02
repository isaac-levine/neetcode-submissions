class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # dp[i][j] = can s[i:] be made with pattern p[j:]?
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True

        for i in range(len(s), -1, -1):
            cur = [False] * (len(p) + 1)
            if i == len(s):
                cur[len(p)] = True
            for j in range(len(p) - 1, -1, -1):
                # 1. if the two characters match or if p is . -> set it to the diagonal.. this is what we'll define as firstMatch

                # 2. if p is a star: the key that makes the code understandable is that we don't deal with a star, until we're one space to the left of it. so we don't have 
                # to deal with any messy skipping or anything like that 
                    # 2a: use this character 0 times --> move to the next character and next pattern thing.
                    # 2b: use this character at least 1 time. --> move to the next character but stay here on the pattern thing? 

                firstMatch = j < len(p) and i < len(s) and (s[i] == p[j] or p[j] == ".")

                # check for star FIRST 
                if j < len(p) - 1 and p[j + 1] == "*":
                    cur[j] = (
                        cur[j + 2] or # don't use the star at all.
                        (firstMatch and dp[j]) # use it at least once: character needs to match but we can continue using it, so leave j in place.
                    )
                else:
                    # next in p is not a star, so we need either a regular match or a '.'
                    cur[j] = firstMatch and dp[j + 1]
            dp = cur

        return dp[0]