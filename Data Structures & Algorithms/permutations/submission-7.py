class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # all possible permutations on array of unique integers --> backtracking 
        # pretty sure basic permutations is just backtracking 

        n = len(nums)
        res = [] 

        def backtrack(cur, pickedIdxs):
            if len(cur) == n:
                res.append(cur[::])
                return
            
            # pick a number to add to cur and keep going
            for i in range(len(nums)):
                if i not in pickedIdxs:
                    # add 
                    cur.append(nums[i])
                    pickedIdxs.add(i)
                    # recurse
                    backtrack(cur, pickedIdxs)
                    # undo
                    cur.pop()
                    pickedIdxs.remove(i)

        
        backtrack([], set())
        return res