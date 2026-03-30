class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        l, r = 0, len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l   
            area = h * w # have to be careful about how you calculate width.
            maxArea = max(maxArea, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea 