class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       

        def isValidRow(row: int) -> bool:
            seen = set() 
            for s in board[row]:
                if s != "." and s in seen:
                    return False
                else:
                    seen.add(s)
            return True


        def isValidCol(col: int) -> bool:
            seen = set()
            for row in range(0, 9):
                cur = board[row][col]
                if cur != "." and cur in seen:
                    return False
                else:
                    seen.add(cur)
            return True


        def isValidBox(startR: int, startC: int) -> bool:
            seen = set()
            for r in range(startR, startR + 3):
                for c in range(startC, startC + 3):
                    cur = board[r][c]
                    if cur != "." and cur in seen:
                        return False
                    else:
                        seen.add(cur)
            return True

        ROWS, COLS = len(board), len(board[0])

        # validate all the rows
        for r in range(9):
            if not isValidRow(r):
                return False

        # validate all the cols 
        for c in range(9):
            if not isValidCol(c):
                return False

        # validate all the sub-boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not isValidBox(r, c):
                    return False

        return True
