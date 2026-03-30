class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        # counts = {}
        
        # "zxyzxyz"
        #   l 
        #     r

        l = 0 
        res = 0
        letters = set() 

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            res = max(res, r - l + 1)
        
        return res
