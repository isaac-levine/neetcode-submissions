class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # return all cells [[r1,c1], etc.] that can reach both the pacific side (top or left) and the atlantic side (bottom or right)
        # a cell can reach the side if there is a path to the side with non-increasing heights

        # idea: reverse the problem 
        # reverse it -> dfs from the border cells, next cell should have height >= current

        # the result coordinates are the cells that exist in both the pacific and atlantic sets...
    
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set() 

        # "visits" (by adding to given set) nodes that are valid path from the border
        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight or (r, c) in visit):
                return
            
            visit.add((r, c))
            dfs(r + 1,  c, visit, heights[r][c])
            dfs(r - 1,  c, visit, heights[r][c])
            dfs(r,  c + 1, visit, heights[r][c])
            dfs(r,  c - 1, visit, heights[r][c])

        # moving vertically
        # left (pacific) and right (atlantic) side 
        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)

        # moving horizontally
        # top (pacific, r = 0), and bottom (atlantic, r = ROWS - 1)
        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res

        


