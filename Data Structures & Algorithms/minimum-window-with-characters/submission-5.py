class Solution:
    def minWindow(self, s: str, t: str) -> str:


        res, resLen = "", float("inf")
        tCounts, window = {}, {}
        for c in t:
            tCounts[c] = 1 + tCounts.get(c, 0)
        need = len(tCounts) # this is how many distinct characters we need to have taken care of 
        have = 0 # how many distinct characters we currently have taken care of 
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) # grow the window from the right
            
            # potentially update the have
            if c in tCounts and window[c] == tCounts[c]:
                have += 1

            # keep shrinking from the left while this window is still valid 
            while have == need:
                
                # potentially update the result 
                if (r - l + 1) < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                
                # shrink the window from the left 
                window[s[l]] -= 1
                if s[l] in tCounts and tCounts[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
            
            
        return res if resLen != float("inf") else ""        