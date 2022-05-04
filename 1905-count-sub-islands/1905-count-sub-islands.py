class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        
        adjacent = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        
        answer = 0
        
        def landCheck(x, y) -> bool:
            check = True
            
            if grid2[x][y] == 0:
                return True
            
            else: #grid[x][y] != 0
                grid2[x][y] = 0
                
                if grid1[x][y] == 0:
                    check = False

                for xi, yi in adjacent:
                    if 0 <= x+xi < m and  0 <= y+yi < n:
                        if grid2[x+xi][y+yi] == 1:
                            check = landCheck(x+xi, y+yi) and check
                                
                return check
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if landCheck(i, j):
                        answer += 1      
            
        return answer