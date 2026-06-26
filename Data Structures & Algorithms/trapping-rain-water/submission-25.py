class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r: # remember that this while condition is checked only at the 
        # beginning of each iteration, so thatts why you dont want <= because it will
        # get handled when the pointers are one space away from each other
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) # we know rightMax is bigger, so this is the binding constraint 
                res += leftMax - height[l] # if leftMax JUST got updated above, then this would be 0. cant be negative b/c of above
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
