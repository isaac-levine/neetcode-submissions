class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        # need a path from one ocean to the other with strictly 


        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set() 
        # Return whether or not this position can reach both oceans 
        def dfs(r, c, visited, prevHeight):
            if (
                (r, c) in visited or 
                r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(r + dr, c + dc, visited, heights[r][c])

        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        
        return [[r, c] for r in range(ROWS) for c in range(COLS) if (r, c) in pacific and (r, c) in atlantic]