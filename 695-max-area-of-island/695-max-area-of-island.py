class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        check = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        solution = 0
        
        def dfs(x: int, y: int):
            check[x][y] = 1
            cnt[0] += 1
            
            if x > 0:
                if grid[x-1][y] == 1 and check[x-1][y] == 0:
                    dfs(x-1, y)
            
            if x < len(grid) - 1:
                if grid[x+1][y] == 1 and check[x+1][y] == 0:
                    dfs(x+1, y)
        
            if y > 0 :
                if grid[x][y-1] == 1 and check[x][y-1] == 0:
                    dfs(x, y-1)
        
            if y < len(grid[0]) - 1:
                if grid[x][y+1] == 1 and check[x][y+1] == 0:
                    dfs(x, y+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and check[i][j] == 0:
                    cnt = [0]
                    dfs(i, j)
                    solution = max(solution, cnt[0])
        
        return solution