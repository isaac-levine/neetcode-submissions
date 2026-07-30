class Solution:
    def checkValidString(self, s: str) -> bool:

        # "((**)"

        # s="()"
        
        openers = []
        stars = []
        

        for i, c in enumerate(s):
            c = s[i]
            if c == "(":
                openers.append(i)
            elif c == "*":
                stars.append(i)
            elif c == ")":
                if openers: # case 1: you have an opener to close.
                    openers.pop()
                elif not openers and stars: # case 2: you dont have an opener to close but you have a star
                    stars.pop()
                elif not openers and not stars: # case 3: you dont have either. failed. 
                    return False

        # process what's leftover. 
        while openers and stars:
            if openers.pop() > stars.pop():
                return False

        return not openers # there can be stars leftover.

                