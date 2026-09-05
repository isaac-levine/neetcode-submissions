class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # quick select:

        # runs over a window nums[l:r+1]
        
        # scanner (j) finds something small? swap with wall (i) and bump wall to the right
        # i : wall, starts at leftmost of window
        # pivot : nums[r] -- moved at the end of the scan
        # j : the scanner that we swap and move the wall using


        target = len(nums) - k

        def quickSort(l, r):

            pivot, i = nums[r], l

            for j in range(l, r): # scanner goes up until the pivot and then we move it at the end
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i] # swap i and j and move i
                    i += 1
            nums[i], nums[r] = pivot, nums[i] # swap i and the pivot 

            # since we have a specific target, we actually know which way we need to go from here. don't need to sort both sides of the pivot. 
            if i > target:
                return quickSort(l, i - 1)
            elif i < target:
                return quickSort(i + 1, r)
            else:
                return nums[i]
        
        return quickSort(0, len(nums) - 1)