class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = [] 

        def backtrack(cur, num_open, num_closed):
            if len(cur) == 2 * n:
                res.append(cur[:])
                return

            # can do a closed if there are more open than closed
            if num_open > num_closed:
                # can put a closed parenthesis
                cur += ")"
                backtrack(cur, num_open, num_closed + 1)
                cur = cur[:-1] # undo the work 
            
            # can do an open as long as we have not already put n
            if num_open < n:
                cur += "("
                backtrack(cur, num_open + 1, num_closed) 


        backtrack("", 0, 0)
        return res