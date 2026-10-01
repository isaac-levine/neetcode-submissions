class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # naturally one queen will get placed on every row, and one queen will get placed on every column,
        # therefore an nxn grid will have n queens placed. 

        boards = [] 


        def dfs(r, cols, posDiag, negDiag, board):

            if r == n:
                boards.append(board[::])

            # backtrack and try every possible placement of column 
            # not every one will lead to a successful board. 
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                row = "." * n
                row = row[:c] + "Q" + row[c+1:]
                board.append(row)

                dfs(r + 1, cols, posDiag, negDiag, board)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board.pop() 

        dfs(0, set(), set(), set(), [])
        return boards 
