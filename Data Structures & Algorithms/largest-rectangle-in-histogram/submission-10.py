class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # heights = [7,1,7,2,2,4]

        maxArea = 0 
        stack = []  # ((0, 7) )

        for i, h in enumerate(heights):
            start = i # 1
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                start = index 
                maxArea = max(maxArea, (i - start) * height)  # why is this times h instead of times height

            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)  # why is this not - 1 

        return maxArea
