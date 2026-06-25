class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            # at any given time, water[i] = min(maxLeft, maxRight) - height[i]. or 0
            if maxLeft <= maxRight: 
                # you know the maximum to your left is your limiting side 
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l] # could this be 0 ? only way, is if new height is bigger, but we're already updating maxLeft 
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        
        return res 

