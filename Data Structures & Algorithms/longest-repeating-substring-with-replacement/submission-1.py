class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        res = maxFreq = l = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) # add this frequency to the map 
            maxFreq = max(maxFreq, freq[s[r]]) # update maxFrequency if necessary

            while ((r - l + 1) - maxFreq) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
