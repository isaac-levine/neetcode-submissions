class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations -> backtracking (n-ary?)

        
        res = [] 
        n = len(nums)

        # decision tree: which num to pick next for the result we're building 
        

        #                       [1,2,3]
        #                       [_,_,_] i = 0 -- where can we put 1
        #               [1,_,_] [_,1,_] [_,_,1] i = 1 -- where can we put 2
        # [1,2,_] [1,_,2]   [2,1,_] [_,1,2]    [2,_,1] [_,2,1] -- where can we put 3?

        def backtrack(i, cur):
            if i == n:
                res.append(cur) # since we're not reusing cur, no need to make a copy
                return
            
            for j in range(n):
                if cur[j] == None:
                    backtrack(i + 1, cur[:j] + [nums[i]] + cur[j + 1:])

        backtrack(0, ([None] * n))
        return res