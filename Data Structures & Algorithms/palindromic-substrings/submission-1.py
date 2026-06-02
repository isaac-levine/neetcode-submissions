class Solution:
    def countSubstrings(self, s: str) -> int:
        
        numPalindromicSubstrings = 0

        for i in range(len(s)):
            # odd length substring
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPalindromicSubstrings += 1
                l -= 1
                r += 1

            # even length substring
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPalindromicSubstrings += 1
                l -= 1
                r += 1

        return numPalindromicSubstrings

