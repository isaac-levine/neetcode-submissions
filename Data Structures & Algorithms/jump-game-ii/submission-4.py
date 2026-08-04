class Solution:
    def jump(self, nums: List[int]) -> int:

        # 2d dp solution with O(n^2) time .. 
        
        # think in terms of 'windows', and the amount of windows is your answer
        

        # each window can reach between the left bound and the right bound of the next window, and the number of windows you have at the end is the minimum amount of jumps required to reach the end
         
        # first window is always [0:0]

        

        if len(nums) <= 1:
            return 0

        # [2,1,2,1,0]

        l = r = 0 
        res = 0

        while r < len(nums) - 1:
            res += 1
            furthest = r + nums[r]

            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i]) 

            # move to the next window
            l = r + 1
            r = furthest
        

        return res