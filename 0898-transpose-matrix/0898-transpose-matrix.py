class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        
        return [[matrix[i][j] for i in range(rows)] for j in range(columns)]
