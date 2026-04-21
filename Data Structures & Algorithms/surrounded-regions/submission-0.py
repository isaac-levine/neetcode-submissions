class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        # reverse approach: just mark the regions that are reachable from the border 0s
        # mark those as visited if they're reachable from the border 0s 

        ROWS, COLS = len(board), len(board[0])
        visit = set() 

        def dfs(r, c):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visit or board[r][c] != "O"
            ):
                return
            
            visit.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        

        # dfs from each of the border 0s, marking any 0s that you can reach as visited
        # sides 
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        

        # loop through the entire board, marking any non-visited 0s as X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"

        
