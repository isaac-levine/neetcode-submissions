class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    

        # key insight: if you graph these points out, you know a point can not extend right any further once it runs into something lower 
        maxArea = 0 
        stack = [] # (index, height) 

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # we know this old rectangle reached its end 
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append((start, h))

        # just look through the remaining stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
