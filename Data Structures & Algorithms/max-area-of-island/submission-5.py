class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0 
        visit = set() 
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal maxArea 
            # skipping everything that is either:
            # 1. off the grid
            # 2. already visited
            # 3. not land
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visit or grid[r][c] != 1
            ):
                return 0
            
            visit.add((r, c))
            up = dfs(r + 1, c)
            down = dfs(r - 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            area = 1 + up + down + left + right
            maxArea = max(maxArea, area)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
        
        return maxArea
        