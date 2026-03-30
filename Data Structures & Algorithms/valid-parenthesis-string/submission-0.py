class Solution:
    def checkValidString(self, s: str) -> bool:

        big, small = 0, 0

        for c in s:
            if c == "(":
                big, small = big + 1, small + 1
            elif c == ")":
                big, small = big - 1, small - 1
            elif c == "*":
                big, small = big + 1, small - 1
            
            if big < 0:
                return False
            if small < 0:
                small = 0 
        
        return small == 0
        