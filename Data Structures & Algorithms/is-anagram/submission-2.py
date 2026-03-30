class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        sCounts = defaultdict(int) 
        # s="racecar"

        # r : 0
        # a : 0
        # c : 0
        # e : 0

        for c in s:
            sCounts[c] += 1

        for c in t:
            if c not in sCounts or sCounts[c] == 0:
                return False
            else:
                sCounts[c] -= 1

        for k, v in sCounts.items():
            if v != 0:
                return False

        return True

