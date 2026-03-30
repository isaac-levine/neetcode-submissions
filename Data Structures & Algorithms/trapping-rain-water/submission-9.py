class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxL, maxR = height[0], height[len(height) - 1] 
        res = 0

        l = 0 
        r = len(height) - 1

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]

        return res
