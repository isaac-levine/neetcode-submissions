class Solution:
    def checkValidString(self, s: str) -> bool:
        
        minOpen = 0
        maxOpen = 0 # this is just for detecting when we have too many right/closers. 

        for c in s:
            # simple cases 
            if c == "(":
                minOpen += 1
                maxOpen += 1
            if c == ")":
                maxOpen -= 1 # only time maxOpen gets decremented. 
                minOpen -= 1

            # could be either an open (max += 1) or a close (min -= 1)
            if c == "*":
                minOpen -= 1
                maxOpen += 1

            # we know this is a failure, because maxOpen only gets decremented by real closers.
            if maxOpen < 0: 
                return False

            # cases like "())" will be caught by the maxOpen check above.
            if minOpen < 0: 
                minOpen = 0

        return minOpen == 0