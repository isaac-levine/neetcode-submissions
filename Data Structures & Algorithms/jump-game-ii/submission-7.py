class Solution:
    def jump(self, nums: List[int]) -> int:
        # process one layer at a time BFS style. and the amount of layers/levels is our answer

        # [2, 4,1,1,1,1]

        # 
        # jumps = 0
        
        l = r = 0
        jumps = 0
        while r < len(nums) - 1:
            jumps += 1
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest

        return jumps

