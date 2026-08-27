class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # biggest possible matrix is 100x100, so definitely can be inefficient algorithm 

        # what if we just cached the LIP from each position? 

        # bfs or dfs? i don't think it matters in terms of finding an increasing path...dfs probably simpler? 

        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0


        cache = {} # (r,c) -> longestIncreasingPath
        # LIP will also act as our visit??? because we know if we are setting a value for it we explore all directions....

        # whenever we save one we should compare against res..so we don't need to iterate again just to return the longest one we've seen
        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prev >= matrix[r][c]:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c])
            )
            return cache[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
                
        return res 

        # don't think we can make this more efficient...we are cachign results, 

        
