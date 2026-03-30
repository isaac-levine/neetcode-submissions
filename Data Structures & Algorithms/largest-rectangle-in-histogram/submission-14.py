class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        
        # heights = [7,1,7,2,2,4]
        maxArea = 0
        stack = [] 

        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)

            stack.append((index, h))


        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea
        
