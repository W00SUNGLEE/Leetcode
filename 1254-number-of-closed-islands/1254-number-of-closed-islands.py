from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        solution = 0
        
        def bfs(a, b) -> bool:
            check = True
            
            deq = deque([])
            
            deq.append((a, b))
            
            while deq:
                x, y = deq.popleft()
                
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    for xi, yi in adjacent:
                        if 0 <= x+xi < m and 0 <= y+yi < n:
                            deq.append((x+xi, y+yi))
                            
                    if x == 0 or x == m-1 or y == 0 or y == n-1:
                        check = check and False
                        
                elif grid[x][y] == 1:
                    continue
                    
                elif grid[x][y] == 2:
                    if x == 0 or x == m-1 or y == 0 or y == n-1:
                        check = check and False
            
            return check
                        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if bfs(i, j):
                        solution += 1
        
        for a in grid:
            print(a)
        
        return solution
        
        
        """
        m = len(grid)
        n = len(grid[0])
        
        adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        solution = 0
        
        visited = []
        
        def closed(x,y) -> bool:
            tmpBool = True
            if grid[x][y] == 0:
                grid[x][y] = 2
                visited.append((x,y))
                
                for xi, yi in adjacent:
                    if 0 <= x+xi < m and 0 <= y+yi < n:
                        if (x+xi, y+yi) not in visited:
                            tmpBool = tmpBool and closed(x+xi, y+yi)
                
                if x == 0 or x == m-1 or y == 0 or y == n-1:
                    return False            
                else:
                    return tmpBool
            
            elif grid[x][y] == 1:
                return True
            
            elif grid[x][y] == 2:
                if x == 0 or x == m-1 or y == 0 or y == n-1:
                    return False
                else:
                    return True
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if closed(i, j):
                        solution += 1
                        for a in grid:
                            print(a)
                        print("------------------------------")
        
        print(visited)
                        
        return solution
        """