class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # binary search to find the correct row
        l, r = 0, len(matrix) - 1 
        lastGoodRow = 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lastGoodRow = mid
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1

        # binary search within this row
        row = matrix[lastGoodRow]
        print("Searching in the row:", row)
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1

        return False
