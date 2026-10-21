class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total = len(grid) ** 2
        seen = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                num = grid[r][c]
                seen[num] = seen.get(num, 0) + 1
      
        for i in range(1, total+1):
            if i in seen and seen[i] == 2:
                a = i
            if i not in seen:
                b = i 
        return [a, b]