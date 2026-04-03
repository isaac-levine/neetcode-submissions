class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for n in nums:
                if n not in cur:
                    cur.append(n)
                    backtrack(cur)
                    cur.pop()

        backtrack([])
        return res  
