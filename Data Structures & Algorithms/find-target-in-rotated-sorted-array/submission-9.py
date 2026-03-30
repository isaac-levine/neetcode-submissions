class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # The search is not about finding where the target is.
        # It's about eliminating where the target can't be. 

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # case 1: we are left of pivot
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                     r = mid - 1
            # case 2: we are right of pivot
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1 
