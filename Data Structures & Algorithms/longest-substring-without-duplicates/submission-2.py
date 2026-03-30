class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        l = 0 
        res = 0
        letters = set() # in O(1) time we can figure out if we've used a character before 

        for r in range(len(s)):
            # while this window is invalid as we're trying to add s[r] to the set
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            res = max(res, r - l + 1)
        
        return res
