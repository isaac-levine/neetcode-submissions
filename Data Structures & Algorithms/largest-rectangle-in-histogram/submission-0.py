class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = [] # (index, height) pairs

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start -= 1 # extend this start index backwards

            stack.append((start, h)) # append not push

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, (len(heights) - index) * height)

        return maxArea

