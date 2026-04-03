class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def backtrack(i, r, c):
            if i == len(word):
                return True # success base case
            elif (r >= ROWS or r < 0 or c >= COLS or c < 0 or
                board[r][c] != word[i] or board[r][c] == '#'):
                return False # failure base case

            board[r][c] = '#' # prevents using the same spot twice in _this_ path
            # do any of the 4 directions lead to a valid path?
            res = (
                backtrack(i + 1, r + 1, c) or 
                backtrack(i + 1, r - 1, c) or 
                backtrack(i + 1, r, c + 1) or 
                backtrack(i + 1, r, c - 1)
            )
            board[r][c] = word[i] # restore it back to what it was -- we already know at this point it's word[i] b/c if not we would have skipped it
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True
        
        return False

