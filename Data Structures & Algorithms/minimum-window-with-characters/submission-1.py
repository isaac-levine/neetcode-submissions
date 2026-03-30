class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        if len(s) < len(t):
            return ""
        elif s == t:
            return s
        
        res, len_res = [-1, -1], float("infinity")
        count_t, window = {}, {}

        # build count_t
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        chars_have, chars_need = 0, len(count_t)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # have all instances of one character
            if c in count_t and window[c] == count_t[c]:
                chars_have += 1
            
            while chars_have == chars_need:
                # update res if this window is smaller
                if (r - l + 1) < len_res:
                    len_res = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    chars_have -= 1

                l += 1

        l, r = res
        return s[l : r + 1] if len_res != float("infinity") else ""
