class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort() # O(n log n)

        res = [] 

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return # success base case
            if i >= len(candidates) or total > target:
                return # fail base case

            # decision: whether or not to include candidates[i]

            # include it
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])

            # don't include it 
            cur.pop() 
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        return res