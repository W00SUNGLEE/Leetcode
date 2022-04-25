from collections import deque

neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        tmp = 0
        deq = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    deq.append((i, j, 0))
        
        while deq:
            i, j, time = deq.popleft()
            
            for di, dj in neighbours:
                newi, newj = i + di, j + dj
                
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] == 1:
                    grid[newi][newj] = 2
                    deq.append((newi, newj, time + 1))
                    tmp = time + 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                
        return tmp
            