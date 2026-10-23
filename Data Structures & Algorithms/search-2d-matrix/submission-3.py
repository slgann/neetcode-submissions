class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix and not matrix[0]:
            return False
        
        r = len(matrix)
        c = len(matrix[0])
        low = 0
        high = (r*c) - 1
        while low <= high:
            mid = (low+high) // 2
            mid_e = matrix[mid // c][mid % c]
            if mid_e == target:
                return True
            elif mid_e > target:
                high -= 1
            else:
                low += 1
        return False       