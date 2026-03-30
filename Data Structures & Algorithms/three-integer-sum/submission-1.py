class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort() # O(n log n)

        for i, a in enumerate(nums): # O(n)
            if a > 0: # if you're starting with a positive, you can't possibly add to 0
                break
            
            if i > 0 and a == nums[i - 1]:
                continue # skip repeats 


            # binary search to find numbers such that l + r + a = 0 
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + a 
                if threeSum > 0:
                    r -= 1 # decrease the sum by shifting the right <-- 
                elif threeSum < 0:
                    l += 1 # increase the sum by shifting the left --> 
                elif threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
                