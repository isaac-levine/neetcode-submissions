class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [1,2,3,4,5]
        # [4,5,1,2,3]
        # [2,3,4,5,1]
        # [5,1,2,3,4]

        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[l] < nums[r]:
                return nums[l]
            elif nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
        
        return nums[l]
