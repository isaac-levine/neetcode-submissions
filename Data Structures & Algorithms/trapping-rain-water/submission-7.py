class Solution:
    def trap(self, height: List[int]) -> int:

        maxLefts = [0] * len(height) 
        maxRights = [0] * len(height) 
        waters = [0] * len(height) 
        res = 0 

        maxRight = 0 
        for i, h in enumerate(height):
            maxRight = max(maxRight, h)
            maxRights[i] = maxRight

        maxLeft = 0
        for i in range(len(height) - 1, -1, -1):
            maxLeft = max(maxLeft, height[i])
            maxLefts[i] = maxLeft

        for i, h in enumerate(height): 
            waters[i] = max(0, min(maxLefts[i], maxRights[i]) - height[i])

        res = 0 
        for w in waters:
            res += w
        return res