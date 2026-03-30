class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # what side of the pivot are we 
            if nums[mid] <= nums[r]:
                # we're in the right sorted portion
                # so you know everything to your right is sorted increasingly 
                # i.e. you know for sure whether it's to your right 
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # we're in the left sorted portion
                # so you know everything to your left is sorted increasingly
                # i.e. you know for sure whether it's to your left
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1 
