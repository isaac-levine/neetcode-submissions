class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        # from each edge point, dfs from it marking everything it can reach by traveling inwards to equal or greater heights.
        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or heights[r][c] < prevHeight):
                return
            
            visit.add((r, c)) # this is the point of the dfs, to update the set with whatever is reachable...
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        
        # can't prepopulate the sets because then you wouldn't be able to start the search...because of the (r,c) in visit: early return
        for r in range(ROWS):
            dfs(r, 0, pacific, 0) 
            dfs(r, COLS - 1, atlantic, 0) 
        
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS - 1, c, atlantic, 0)
        
        res = [] 
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        return res
        