class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # at any point in time, we only need to know the minimum number of openers there could be
        # and the maximum number of openers there could be (the range comes from how many stars you choose to use.)

        leftMin = 0
        leftMax = 0

        # if you see an open, increment both.
        # if you see a close, decrement both.
        # if you see a star, acount for both scenarios. decremeent min (use as closer) and incremement max (use another opener)

        # if maxOpen ever < 0. then return False because that means you had too many closers

        # if you end with minOpen > 0 then return False because that means you didnt see enough closers / stars. 

        
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            if c == ")":
                leftMin -= 1
                leftMax -= 1
            if c == "*":
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False # too many closers 
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0
            