class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # loop through tokens
            # if its a number -> add it to the stack
            # operation --> do the operation with the two popped numbers from the stack

        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                n1, n2 = stack.pop(), stack.pop() 
                if t == "+":
                    stack.append(n2 + n1)
                elif t == "-":
                    stack.append(n2 - n1)
                elif t == "/":
                    stack.append(int(n2 / n1))
                elif t == "*":
                    stack.append(n2 * n1)

        return stack.pop() 
