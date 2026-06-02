class Solution:
    def longestPalindrome(self, s: str) -> str:

        resL, resR = 0, 0 
        resLen = 0 

        for i in range(len(s)):
            # odd case 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resL, resR = l, r
                l -= 1
                r += 1


            # even case 
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resL, resR = l, r
                l -= 1
                r += 1

        return s[resL : resR + 1]
        