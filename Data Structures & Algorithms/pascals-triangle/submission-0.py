class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        
        res = [[1], [1, 1]] 

        for i in range(2, numRows):
            newRow = [1]
            prev = res[i - 1]
            for j in range(len(prev) - 1):
                pair = prev[j] + prev[j + 1]
                newRow.append(pair)
            newRow.append(1)

            res.append(newRow)
        return res
