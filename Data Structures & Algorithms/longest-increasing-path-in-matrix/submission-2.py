class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        longest = 1
        # (r,c) -> LIP starting from matrix[r][c] or can just do 2d array
        # cache = {}
        cache = [[0] * COLS for _ in range(ROWS)]

        # LIP in matrix starting at point (r, c), pass prevVal to ensure increasing order
        def findLongest(r, c, prevVal):
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prevVal:
                return 0
            if cache[r][c] > 0: # already know this point's LIP 
                return cache[r][c]
            directions = [[1,0], [-1,0], [0, 1], [0,-1]]
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + findLongest(r + dr, c + dc, matrix[r][c]))
            # res = max(res, 1 + findLongest(r + 1, c, matrix[r][c]))
            # res = max(res, 1 + findLongest(r - 1, c, matrix[r][c]))
            # res = max(res, 1 + findLongest(r, c + 1, matrix[r][c]))
            # res = max(res, 1 + findLongest(r, c - 1, matrix[r][c]))
            cache[r][c] = res
            return res
            # cache[r][c] = 1 + max(cache[r+1][c] , cache[r-1][c] , cache[r][c+1] , cache[r][c-1] )

        print(cache)

        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, findLongest(r, c, -1))
        return longest 