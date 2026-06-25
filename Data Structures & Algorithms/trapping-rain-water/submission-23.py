class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers closing inward. Each side's wall is a CERTIFIED LOWER
        # BOUND on that side's true max, not necessarily the true max. The
        # shorter certified wall is the true water level for the cell it points at.

        lo, hi = 0, len(height) - 1
        trapped = 0
        leftWall, rightWall = height[lo], height[hi]

        while lo < hi:
            if leftWall < rightWall:
                # leftWall is the shorter wall -> binding constraint.
                # true right max >= rightWall > leftWall, so right can't lower the level here.
                lo += 1
                leftWall = max(leftWall, height[lo])
                trapped += leftWall - height[lo]   # >= 0: leftWall just maxed against height[lo]
            else:
                # rightWall is binding by symmetry.
                hi -= 1
                rightWall = max(rightWall, height[hi])
                trapped += rightWall - height[hi]
        return trapped