class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # width = r - l + 1
        # height = min(heights[l:r+1])

        # [7,1,7,2,2,4] --> 8
        # [1,3,7]       --> 7

        maxArea = 0
        stack = [] # pair of (index, height) 

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                # pop the height
                # check the max rectangle from that height
                # extend current height backwards
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) 
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea 
