class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # candidates may contain duplicates
        # return list of unique combinations (differentiated by frequency of number)

        candidates.sort() 
        res = [] 

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return # success base case
            if i >= len(candidates) or total > target:
                return # fail base case
            
            # include this num
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i]) # continue on, each element may be only be chosen at most once

            # don't include this num (or any future instances of it)
            cur.pop() 
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]: # skip over future instances of this num
                i += 1
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res 