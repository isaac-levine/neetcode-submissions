class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # this is the most pure and basic intro to backtracking problem 

        # - nums are unique 
        # - solution set must not contain duplicates --> always move i + 1 regardless of decision whether to include

        
        res = [] 

        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return # success base case
            
            # include this number
            cur.append(nums[i])
            backtrack(i + 1, cur)
             
            # don't include this number 
            cur.pop()
            backtrack(i + 1, cur)
            
        backtrack(0, [])
        return res 