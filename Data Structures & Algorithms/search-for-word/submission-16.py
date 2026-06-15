class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # start a dfs from every instance of word[0]

        ROWS, COLS = len(board), len(board[0])

        visit = set() 
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] != word[i]: 
                return False 

            visit.add((r, c))
            
            if (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1)
            ):
                return True

            visit.remove((r, c)) # need to remember this part

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visit = set()
                    if dfs(r, c, 0):
                        return True
        return False



            