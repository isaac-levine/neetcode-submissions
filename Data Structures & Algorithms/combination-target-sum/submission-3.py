class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # nums are distinct * -- so there's no need to deal with duplicates in the input -- but can have duplicates in the output 
        # return a list of all unique COMBINATIONS of nums where the chosen numbers sum to target
        # don't have to use all nums 
        # combinations are differentiated purely by counts, can repeat nums 
        # combinations = order does not matter 

        res = [] 
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return # success base case
            if i >= len(nums) or total > target:
                return # failure base case

            # include this num
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i]) # can repeat this num any amount of times, so don't inc. i

            # don't include this num
            cur.pop()
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        return res 