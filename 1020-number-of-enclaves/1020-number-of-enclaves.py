from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        solution = 0
        
        def dfs(x, y):
             if grid[x][y] == 1:
                grid[x][y] = 0
                for xi, yi in adjacent:
                    if 0 <= x+xi < m and 0 <= y+yi < n:
                        if grid[x+xi][y+yi] == 1:  
                            dfs(x+xi, y+yi)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        for i in range(1,m-1):
            dfs(i, 0)
            dfs(i, n-1)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    solution += 1
            
        return solution