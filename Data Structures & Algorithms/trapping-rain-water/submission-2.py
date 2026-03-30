class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        N, res = len(height), 0
        l, r = 0, N - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] # never negative since we get leftMax first
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r] # ""

        return res
                            