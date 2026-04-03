class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # O(n log n)
        res = []

        def backtrack(cur, i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            # include this number
            cur.append(nums[i])
            backtrack(cur, i + 1)

            cur.pop() 

            # don't include this number (or future instances of it)
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(cur, i + 1)

        backtrack([], 0)
        return res