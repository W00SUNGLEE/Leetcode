class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        adjacent = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        solution = 0
        
        def landCheck(x, y):
            if grid[x][y] == "0":
                return
            
            else: #grid[x][y] != 0
                grid[x][y] = "0"
                for xi, yi in adjacent:
                    if 0 <= x+xi < m and  0 <= y+yi < n:
                        if grid[x+xi][y+yi] == "1":
                            landCheck(x+xi, y+yi)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    landCheck(i, j)
                    solution += 1
                
        
                        
        return solution