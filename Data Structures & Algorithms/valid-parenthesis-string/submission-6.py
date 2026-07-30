class Solution:
    def checkValidString(self, s: str) -> bool:

        # "((**)"

        # s="()"
        
        openers = []
        stars = []
        

        for i, c in enumerate(s):
            c = s[i]
            if c == "(":
                print("found an opener")
                openers.append(i)
            elif c == "*":
                stars.append(i)
            elif c == ")":
                print("found a closer")
                if openers: # case 1: you have an opener to close.
                    print("--- popped an opener")
                    openers.pop()
                elif not openers and stars: # case 2: you dont have an opener to close but you have a star
                    print("--- popped a star")
                    stars.pop()
                elif not openers and not stars: # case 3: you dont have either. failed. 
                    return False

        # process what's leftover. 
        while openers:
            if not stars:
                return False
            openerIndex = openers.pop() # this is the furthest right openerIndex. 
            # is there a star index to it's right?
            starIndex = stars.pop()
            if openerIndex > starIndex:
                return False

        return True

                