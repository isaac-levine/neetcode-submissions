class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq = [0] * 26

        for c in s1:
            freq[ord(c) - ord('a')] += 1 # remember the ord(c) function.

        # we have the frequency of all characters in s1

        # want to know, can they all fit in s2

        
        win_freq = [0] * 26
        l = 0

        for r in range(len(s2)):
            win_freq[ord(s2[r]) - ord('a')] += 1

            # when window size is > len(s1), shrink from the left 
            w = r - l + 1
            if w > len(s1):
                win_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            # check frequency, and early return if possible
            if win_freq == freq:
                return True
        
        return False
