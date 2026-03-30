class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # there are duplicates and we can use duplicates 
        # return list of all unqiue combinations of candidates where sum == target
        # solution set must not contain duplicate combinations  (sort?)

        # sort the candidates O(N log N)

        # backtrack function
            # reject if out of bounds or sum > target

            # include this candidate 

            # don't include this candidate (and never include it)


        res = []
        candidates.sort() # O(N log N)

        # [1,2,3,4,5]

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
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i + 1, subset, curSum)

        backtrack(0, [], 0)
        return res


        