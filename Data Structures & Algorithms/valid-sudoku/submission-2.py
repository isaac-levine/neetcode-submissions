class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Each row must contain the digits 1-9 without duplicates.
        # Each column must contain the digits 1-9 without duplicates.
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

        ROWS, COLS = len(board), len(board[0])

        # loop through each of the 9 (boxes) and check that box 
        # loop through each row, checking that row 
        # loop through each column, checking that column

        # check the rows
        for r in range(ROWS):
            row = board[r]
            numsInRow = set()
            for num in row:
                if num in numsInRow: 
                    return False
                elif num != ".":
                    numsInRow.add(num)

        
        # check the cols 
        for c in range(COLS):
            numsInCol = set() 
            for r in range(ROWS):
                num = board[r][c]
                if num in numsInCol:
                    return False
                elif num != ".":
                    numsInCol.add(num)

        # check the boxes
        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                numsInBox = set()
                for rr in range(0, 3):
                    for cc in range(0, 3):
                        num = board[r + rr][c + cc]
                        if num in numsInBox:
                            return False
                        elif num != ".":
                            numsInBox.add(num)

        return True


