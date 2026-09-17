class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # I think since we have the full array we can just do quick select....
        # pivot at the right edge, then a wall (i) that we swap  

        n = len(nums)
        target = n - k # kth largest also means n - k + 1 smallest, so we want the n - k index in asc. order

        def quickSelect(l, r):
            
            i = l # i is the wall, the pivot is nums[r]
            for j in range(l, r):
                # compare j to pivot and move everything smaller than pivot to the left of the wall
                # bump the wall
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            # move the pivot wherever the wall ended
            nums[r], nums[i] = nums[i], nums[r]
            if i == target:
                return nums[i]
            # if we didn't find the answer, we know we only need to recurse in one direction instead of both
            elif i > target:
                # recurse left
                return quickSelect(l, i - 1)
            else:
                # recurse right 
                return quickSelect(i + 1, r)

        
        return quickSelect(0, len(nums) - 1)
