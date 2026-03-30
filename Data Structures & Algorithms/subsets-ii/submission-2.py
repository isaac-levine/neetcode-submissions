class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur[::])
                return
            
            # use it
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

            # don't use it (and never use it)
            while i + 1 < len(nums) and nums[i] == nums[i+1]: # while the next one is the same
                i += 1

            backtrack(i + 1, cur)



        backtrack(0, [])
        return res