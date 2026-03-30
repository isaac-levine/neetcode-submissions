class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort() # O(n log n)

        for i, a in enumerate(nums):
            if a > 0:
                break # cant possibly find a sum(a,b,c) == 0 b/c we sorted
            
            if i > 0 and a == nums[i - 1]:
                continue # skip repeat starters 

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
    
        return res