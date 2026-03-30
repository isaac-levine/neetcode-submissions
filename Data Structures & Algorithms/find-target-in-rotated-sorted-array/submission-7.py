class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # nums = [3,4,5,6,1,2], target = 1
        # nums = [3,5,6,0,1,2], target = 4

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
        
        # return it if we got or else -1 
        mid = (l + r) // 2
        return mid if nums[mid] == target else -1  
