class Solution:
    def isValid(self, s: str) -> bool:
       
        # every opener must be closed by the same type of closer
        # openers must be closed in the correct order
        # closers must have a corresponding opener

        closeToOpen = {'}' : '{',
                       ')' : '(',
                       ']' : '['}
        stack = [] 

        for c in s:
            if c in closeToOpen.values(): # opener 
                stack.append(c)
            else: # closer
                # the top of the stack must be a corresponding opener
                if len(stack) == 0 or stack.pop() != closeToOpen[c]:
                    return False
       
        return len(stack) == 0
