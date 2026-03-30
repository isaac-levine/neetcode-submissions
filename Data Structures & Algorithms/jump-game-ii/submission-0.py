class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        l = r = 0 # what portion of the array is currently being used for BFS


        while r < len(nums) - 1:
            farthest = 0 # the farthest locaiton that we can jump to from this window
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1
        

        return jumps
