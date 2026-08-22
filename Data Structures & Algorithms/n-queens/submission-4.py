class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # all distinct solutions --> backtracking? 
        # n is only up to size 8, so backtracking so could be really slow like O(n!) 

        # if something is at (0,1), no one can be at (1,2) or (2,3)
        # or other diagonal no one can be at (2,0)

        # relation between a placement that we try and the diagonals it blocks? 

        #         (1,3)
        #     (2,2)  (2,4)
        #   (3,1)       (3,5)
        # (4,0)           (4,6)

        # / "posDiag"
        # going down to the left, r increases, c decreases
        # going up to the right, r decreases, c increases
        # --> so (r + c) stays constant

        # \ "negDiag"
        # going up to the left, r and c both decrease by 1
        # going down to the right, r + c both increase by 1
        # --> so (r - c) stays constant

        # backtrack and try placing a queen on every position. 
        # you can place a queen at a position if (r + c) and (r - c) do not violate any taken diagonals
        # once you have successfully placed n queens on a board, add that board to the result 

        # another key insight: 1 queen per row and col no matter what. n queens on an n x n grid...
        # this makes the recursion so much simpler because you just start with row 0 and go through all columns,
        # moving to the next row from each of those columns that you try....

        res = [] 
        board = [["."] * n for _ in range(n)]
        col, posDiag, negDiag = set(), set(), set()
        def backtrack(r):
            if r == n: # we know we have added a queen to every row from [0,n-1] so we're done  
                boardCopy = ["".join(row) for row in board]
                res.append(boardCopy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue 
                # add the queen to this position
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # recurse
                backtrack(r + 1)

                # remove it
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c) # is it 

            
        backtrack(0)
        return res 
            