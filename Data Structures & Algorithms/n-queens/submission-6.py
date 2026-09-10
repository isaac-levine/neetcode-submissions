class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        # no 2 queens can attack eachother...i.e. 1 queen per row, column, and diagonal -- i remember this insight from last time 

        # return all distinct valid boards
         
        
        res = [] 
        board = [["."] * n for _ in range(n)]

        # lets just add to boards everytime we find a complete board ...
        # now i remember that we want to process row by row and keep track of the two diagonals as well as the columns that have been used 
        # but what do we memoize? is there any DP going on in this problem? wait the board is really small, so maybe we can be kinda brute forcy.
        # is it really just a normal graph (grid) traversal problem? i thought there was some dp going on here. 

        # one diagonal is calculated using (r - c) and one is calculated using (r + c)
        cols, posDiag, negDiag = set(), set(), set()

        def backtrack(r):
            if r == n:
                boardCopy = ["".join(row) for row in board]
                res.append(boardCopy)
                return

            # check every col to find a spot to place this queen on this board
            for c in range(n):
                # found a good placement
                if c not in cols and (r - c) not in negDiag and (r + c) not in posDiag:
                    # add
                    posDiag.add((r + c))
                    negDiag.add((r - c))
                    cols.add(c)
                    board[r][c] = "Q"

                    # recurse
                    backtrack(r + 1)

                    # remove
                    posDiag.remove((r + c))
                    negDiag.remove((r - c))
                    cols.remove(c)
                    board[r][c] = "."
        
        backtrack(0)
        return res