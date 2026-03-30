class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # does s2 contain a permutation of s1?
        # i.e. are all of the characters (and counts) of s1 contained in s2? 

        # s1 = "abc", s2 = "lecabee"

        # 1.) get the counts of the characters in s1 
        freq = [0] * 26
        for c in s1:
            freq[self.pos(c)] += 1

        # 2.) move a sliding window of size len(s1) across s2
        win_freq = [0] * 26
        l = 0
        for r in range(len(s2)):
            win_freq[self.pos(s2[r])] += 1

            w = r - l + 1 
            if w > len(s1): # window is too big, need to shrink it from the left
                win_freq[self.pos(s2[l])] -= 1
                l += 1

            if win_freq == freq:
                return True

        return False
            

    def pos(self, c: str) -> int: 
        return ord(c) - ord('a')
