class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        # we are looking for a permutation of s1 in s2

        # ~~ s1 ~~
        # a : 1
        # b : 1
        # c : 1

        # ~~ window of s2 ~~ 
        # ...

        # get the counts of the characters in s1 
        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        # print(s1_freq)
        
        win_freq = [0] * 26
        l = 0
        for r in range(len(s2)):
            win_freq[ord(s2[r]) - ord('a')] += 1 

            # When window size > len(s1), shrink from left
            if r - l + 1 > len(s1):
                win_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if win_freq == s1_freq:
                return True

        return False 

