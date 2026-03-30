class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort() # O(N log N)

        def backtrack(i, subset, curSum):
            if curSum == target:
                res.append(subset[::])
                return
            elif i == len(candidates) or curSum > target: # fail base case
                return

            # include this candidate
            subset.append(candidates[i])
            backtrack(i + 1, subset, curSum + candidates[i])
            subset.pop()

            # don't include this candidate (and never do)
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i + 1, subset, curSum)

        backtrack(0, [], 0)
        return res


        