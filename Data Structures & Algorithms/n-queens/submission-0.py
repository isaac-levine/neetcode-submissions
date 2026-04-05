class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # we'll keep track of each columns, pos diagonals, and neg diagonals that we place queens in. 
        # we don't need to track rows because we'll just move to the next row after placing a queen.

        # on neg-diagonals: (r-c) remains constant -- so we can name the "0" neg-diagonal for example 
        # on pos-diagonals: (r+c) remains constant 

        # decision tree will be row by row. we first try a queen in each position of row 0, then each position of row 1. for each of those decisions, etc. 

        res = [] 
        board = [["."] * n for i in range(n)]

        col = set() 
        pos_diag = set() # determined by (r+c)
        neg_diag = set() # determined by (r-c)

        
        def backtrack(r):
            if r == n:
                board_copy = ["".join(row) for row in board]
                res.append(board_copy)
                return

            # try every position (column) in the current row for placing a queen
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue # not allowed to use this (r, c) position
                
                # mark this position as used.
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # clean up our work
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res