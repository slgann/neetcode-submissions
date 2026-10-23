class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                num.append(matrix[r][c])
        
        for i in num:
            if i == target:
                return True
        return False
        