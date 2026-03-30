class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1 
        res = nums[0]

        while l <= r:
            mid = (l + r) // 2

            res = min(res, nums[mid]) 

            # am i in the left sorted portion or the right
            # is the right bigger than me? then i'm in the right.
            if nums[r] >= nums[mid]:
                # in right sorted portion 
                r = mid - 1
            else:
                l = mid + 1

        return res 
