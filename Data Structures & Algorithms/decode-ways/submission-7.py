class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 0

        # cur, one, two 

        for i in range(len(s) - 1, -1, -1):
            cur = 0
            # 1. single digit case
            if s[i] in "123456789":
                cur += one
            
            # 2. two digit case
            #   2a. 1 and 0-9
            #   2b. 2 and 0-6
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cur += two

            two = one
            one = cur

        return one