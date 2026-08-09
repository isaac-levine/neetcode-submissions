class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # water can only flow to cell with height equal or lower
        # reachability: use dfs or bfs 

        ROWS, COLS = len(heights), len(heights[0])
        
        atlantic = set()
        pacific = set() 

        # flip the problem: water will be flowing backwards from the coast in and we will
        # add any valid points along the way to our path set.
        # our path is kind of just an accumulator that tells us what is reachable 
        def dfs(r, c, path, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight or (r, c) in path:
                return

            path.add((r, c))

            dfs(r + 1, c, path, heights[r][c])
            dfs(r - 1, c, path, heights[r][c])
            dfs(r, c + 1, path, heights[r][c])
            dfs(r, c - 1, path, heights[r][c])

        
        for c in range(COLS):
            dfs(0, c, pacific, -1) # gather all points starting from top row (pacific)
            dfs(ROWS - 1, c, atlantic, -1) # gather all points starting from bottom row (atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific, -1) # gather all points starting from left col (pacific)
            dfs(r, COLS - 1, atlantic, -1) # gather all points starting from right col (atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res