from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
                

        res = [0] * len(temperatures) 
        stack = [] # stores pairs of (value, index) 
        
        for i in range(len(temperatures)):
            curVal = temperatures[i]

            # current value is greater than stack value
            while stack and curVal > stack[-1][0]:
                _, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx 
            
            stack.append((curVal, i))

        return res 
