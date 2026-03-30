class Solution:
    def isValid(self, s: str) -> bool:

        # ([{}])
        # stack = 
       
        pairs = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            # Closer
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        return not stack
