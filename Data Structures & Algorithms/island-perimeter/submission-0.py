class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    total += 4
                    if c + 1 < len(grid[0]) and grid[r][c+1] == 1:
                        total -= 2
                    if r + 1 < len(grid) and grid[r+1][c] == 1:
                        total -= 2
                
        return total