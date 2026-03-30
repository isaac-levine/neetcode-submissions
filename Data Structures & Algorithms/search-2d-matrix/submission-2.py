class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        # 1. binary search to find the target row
        # goal: find the greatest head target[r][0] that is <= target, b/c you know everything in that row is >= head.

        finalRow = 0
        top, bot = 0, ROWS - 1  
        while top <= bot:
            r = (top + bot) // 2
            head = matrix[r][0]
            print("checking row ", r, " which beings with a ", head)
            if head < target:
                finalRow = max(finalRow, r) 
                top += 1
            elif head > target:
                bot -= 1
            else:
                return True

        print("DEBUG: target must be in row " , finalRow)

        # 2. binary search within that row to find the target index. return t/f 
        row = matrix[finalRow]
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r -= 1
            else:
                l += 1
            
        return False
          
