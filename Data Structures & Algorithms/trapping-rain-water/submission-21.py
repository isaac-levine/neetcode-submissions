class Solution:
    def trap(self, height: List[int]) -> int:
        

        l, r = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) # you know rightMax is bigger because of the if branch
                res += leftMax - height[l] # you know this is never negative because of the line above. 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res