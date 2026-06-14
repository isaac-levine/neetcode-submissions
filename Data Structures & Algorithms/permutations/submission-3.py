class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        res = [] 

        def backtrack(cur, used):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    backtrack(cur, used)
                    cur.pop()
                    used[i] = False
        
        backtrack([], [False] * len(nums))
        return res
