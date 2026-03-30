class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(i, cur, curSum):
            if curSum == target:
                res.append(cur[:])
                return
            elif curSum > target or i == len(nums):
                return
            
            # include this one (maybe again)
            cur.append(nums[i])
            backtrack(i, cur, curSum + nums[i])

            # skip this one 
            cur.pop()
            backtrack(i + 1, cur, curSum)

        backtrack(0, [], 0)
        return res

        