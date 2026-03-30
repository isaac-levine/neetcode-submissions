class Solution:
    def jump(self, nums: List[int]) -> int:

        res, l, r = 0, 0, 0

        while r < len(nums) - 1:
            farthestJumpInWindowLocation = 0
            for i in range(l, r + 1):
                farthestJumpInWindowLocation = max(farthestJumpInWindowLocation, i + nums[i])
            l = r + 1
            r = farthestJumpInWindowLocation
            res += 1
        
        return res
