class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res, resLen = "", float("inf")
        
        need = 0 
        tCounts, window = {}, {} 
        for c in t:
            tCounts[c] = 1 + tCounts.get(c, 0)
        have, need = 0, len(tCounts) # need represents the number of letters we need regardless of their count

        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            cur = s[l:r+1]

            if c in tCounts and window[c] == tCounts[c]:
                have += 1

            while have == need:
                cur = s[l:r+1]
                if len(cur) < resLen:
                    resLen = len(cur)
                    res = cur
                window[s[l]] -= 1 # shrink from the left
                if s[l] in tCounts and window[s[l]] < tCounts[s[l]]:
                    have -= 1 # check if shrinking caused us to lose a character
                l += 1

        return res if resLen != float("inf") else ""


                

            


        