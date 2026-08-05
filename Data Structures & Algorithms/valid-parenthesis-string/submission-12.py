class Solution:
    def checkValidString(self, s: str) -> bool:
        

        # ((**)
        # minLeft = 0
        # maxLeft = 3


        minLeft, maxLeft = 0, 0 

        for c in s:
            if c == "(":
                minLeft += 1
                maxLeft += 1
            if c == ")":
                maxLeft -= 1
                minLeft -= 1
            if c == "*":
                minLeft -= 1
                maxLeft += 1

            if maxLeft < 0:
                return False
            if minLeft < 0:
                minLeft = 0

        return minLeft == 0