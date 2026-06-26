class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # we are flipping the problem. starting from each edge square (pacific and atlantic square), we want to know 
        # what squares are reachable from those and just return the intersection of those two sets

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
            dfs(0, c, pacific, 0) # start the dfs from the top row touching the pacific
            dfs(ROWS - 1, c, atlantic, 0) # start the dfs from the bottom row touching the atlantic

        for r in range(ROWS):
            dfs(r, 0, pacific, 0) # start the dfs from the left column touching the pacific
            dfs(r, COLS - 1, atlantic, 0) # start the dfs from the right column touching the atlantic 

        
        return [[r, c] for r in range(ROWS) for c in range(COLS) if (r, c) in pacific and (r, c) in atlantic]