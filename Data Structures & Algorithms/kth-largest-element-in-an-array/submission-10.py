class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # we want "kth largest" -> len(nums) - k smallest.
        target = len(nums) - k 

        def quickSelect(l, r):
            pivot, i = nums[r], l

            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i] # swap i and j
                    i += 1 # don't really understand what mechanism this is 
            nums[r], nums[i] = nums[i], nums[r] # swap pivot and i
            
            # based on what pivot ends up being, we know which way we have to go
            # we don't have to explore both sides..we can save time and just explore the one 
            # where we know the answer must be 

            # compare index where pivot ended up (i) against target
            if i < target: return quickSelect(i + 1, r)
            if i > target: return quickSelect(l, i - 1)
            else: return nums[i] # make sure to return the value at i, not the index
        
        return quickSelect(0, len(nums) - 1)
        
