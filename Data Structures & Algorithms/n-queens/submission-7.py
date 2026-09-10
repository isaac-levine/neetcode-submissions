class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        def dfs(r, cols, posDiag, negDiag, board):
            if r == n:
                res.append(board)
                return

            # check every col to find a spot to place this queen on this board
            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue
                dfs(r + 1,
                    cols | {c},
                    posDiag | {r + c},
                    negDiag | {r - c},
                    board + ["." * c + "Q" + "." * (n - c - 1)] # add this row to board
                )
        
        dfs(0, set(), set(), set(), [])
        return res