class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if len(s) < len(t) or t == "":
            return "" 

        count_t, window = {}, {}  
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t) # need all characters in t to be satisified 

        res, resLen = [-1, -1], float("inf") # default value for the result
        l = 0 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) 

            if c in count_t and window[c] == count_t[c]: # JUST satisified a new character 
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:    
                    res = [l, r]
                    resLen = (r - l + 1) 
                # pop from the left to remove a character 
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]: # check if we JUST broke a character satisfaction
                    have -= 1 
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else "" 


            
