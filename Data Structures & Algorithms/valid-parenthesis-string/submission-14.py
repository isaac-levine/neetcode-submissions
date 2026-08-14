class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # because this is not contiguous and you need to support a range of possibilities,
        # i know its DP 

        # or wait is it greedy? can we commit to a local optima irrerversibly?

        dp = [False] * len(s)
        minOpen = maxOpen = 0

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                minOpen += 1
                maxOpen += 1
            elif c == ")":
                minOpen -= 1
                maxOpen -= 1
            elif c =="*":
                minOpen -= 1 # use a closer
                maxOpen += 1 # use opener 
                # or use nothing, and that's fine because window got bigger?

            if minOpen < 0:
                minOpen = 0 # ?
            
            if maxOpen < 0:
                return False

        return minOpen <= 0 <= maxOpen

