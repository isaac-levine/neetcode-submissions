class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        res = 0
        
        l, r = 0, len(height) - 1

        # while l < r:

        maxLeft = [0] * n
        prevMax = 0
        for i in range(0, n):
            maxLeft[i] = prevMax
            prevMax = max(prevMax, height[i])

        maxRight = [0] * n
        prevMax = 0
        for i in range(n - 1, -1, -1):
            maxRight[i] = prevMax
            prevMax = max(prevMax, height[i])

        mins = [0] * n
        for i in range(n):
            mins[i] = min(maxLeft[i], maxRight[i])

        print(maxLeft)
        print(maxRight)
        print(mins)
        print(height)

        for i in range(n):
            diff = mins[i] - height[i]
            res += diff if diff >= 0 else 0

        return res


