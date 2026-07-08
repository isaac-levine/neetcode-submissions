class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        target = len(nums) - k
        l, r = 0, len(nums) - 1

        while True: 
            # we are partioning the subset [l, r] with pivot being nums[r]
            # pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i] # swap i and j when j < p
                    i += 1
            nums[i], nums[r] = nums[r], nums[i] # swap i and pivot when done 

            # either we're done, we continue left, or we continue right
            if i == target:
                return nums[i]
            elif i < target:
                l = i + 1
            else:
                r = i - 1
