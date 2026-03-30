class Solution:
    def trap(self, height: List[int]) -> int:
       

        # the core insight: at any position i, you need to know what is the max to my left and what is the max to my right. 
        # you only need to know the max on the side that you're processing... 



        l, r = 0, len(height) - 1 
        leftMax, rightMax = height[l], height[r] 
        res = 0 

        while l < r:
            if leftMax <= rightMax:
                l += 1
                res += max(0, leftMax - height[l]) # nit: youactually know that min(leftMax, rightMax) must be leftMax here.
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                res += max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])

        return res 
