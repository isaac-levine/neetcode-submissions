class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set() 
        

        # water can flow to equal or lower height 

        # pacific set and atlantic set 
        # reachability -> DFS? (don't think it matters for reachability problems if its BFS or DFS)
        # mark your visit path as you go (mutate the pacific and atlantic sets and then just return the intersection of the sets)

        def dfs(r, c, path, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or prevHeight > heights[r][c]:
                return 

            path.add((r, c))
            dfs(r + 1, c, path, heights[r][c])
            dfs(r - 1, c, path, heights[r][c])
            dfs(r, c + 1, path, heights[r][c])
            dfs(r, c - 1, path, heights[r][c])

        for r in range(ROWS):
            # left side pacific, right side atlantic
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)

        for c in range(COLS):
            # top row pacific, bottom row atlantic
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)

        res = [] 
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])
        return res
