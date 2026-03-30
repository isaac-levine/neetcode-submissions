class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[0] 

        while l <= r:
            # sorted normally
            if nums[l] < nums[r]:
                smallest = min(smallest, nums[l])
                break

            mid = (l + r) // 2
            smallest = min(smallest, nums[mid])

            # are we going to search to the right or to the left?
            # depends on if we're in the left sorted portion
            if nums[mid] >= nums[l]:
                # we're in the left sorted portion and want to search to the right
                l = mid + 1 
            else:
                # we're in the right sorted portion and want to search to the left
                r = mid - 1

        return smallest
