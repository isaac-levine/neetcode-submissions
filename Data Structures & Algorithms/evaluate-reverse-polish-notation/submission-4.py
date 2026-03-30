class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 

        for t in tokens:
            if t in "+-*/": # operation case
                numB = stack.pop()
                numA = stack.pop()
                if t == "+":
                    stack.append(numA + numB)
                elif t == "-":
                    stack.append(numA - numB)
                elif t == "*":
                    stack.append(numA * numB)
                elif t == "/":
                    # casting to int is the proper way to divide towards 0 
                    # using // will just truncate towards negative inifnity
                    stack.append(int(numA / numB))
            else: # number case
                stack.append(int(t))

        return stack.pop() 
