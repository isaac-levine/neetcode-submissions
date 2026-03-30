class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx = 0
        resLen = 0
        
        def expand(l, r):
            nonlocal resIdx, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resLen):
                    resIdx = l
                    resLen = r - l + 1 
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[resIdx : resIdx + resLen]