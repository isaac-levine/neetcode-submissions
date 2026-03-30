class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # num >= stack --> pop it off, put num there,

        # set to 0 if stack is empty 

        # num < stack --> 1, put num on top of the stack 

        # [30,38,30,36,35,40,28]
        # stack = (40, 5), (38, 1), (30, 0)
        # temp, i = 
        # result = [1, 4, 1, 2, 1, 0, 0]

        result = [0] * len(temperatures)
        stack = []
        stack.append((temperatures[-1], len(temperatures) - 1))

        for i in range(len(temperatures) - 2, -1, -1):
                temp = temperatures[i]
                while stack and temp >= stack[-1][0]:
                    stack.pop() 
                result[i] = (stack[-1][1] - i) if stack else 0
                stack.append((temp, i))
        
        return result
        

