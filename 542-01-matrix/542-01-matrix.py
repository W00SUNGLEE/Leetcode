from collections import deque

neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat = [[(x if x == 0 else float('inf')) for x in y] for y in mat]
        print(mat)
        
        deq = deque()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    deq.append((i, j))
                    
        while deq:
            
            i, j= deq.popleft()
            
            for di, dj in neighbours:
                newi, newj = i + di, j + dj
                
                if 0 <= newi < len(mat) and 0 <= newj < len(mat[0]) and mat[newi][newj] > mat[i][j] + 1:
                    mat[newi][newj] = mat[i][j] + 1
                    deq.append((newi, newj))

                    
        return mat
        
        
        """
        dp = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        seen = set()
                    
        def dfs(x: int, y: int):
            if not (0 <= x < len(mat) and 0 <= y < len(mat[0])):
                return 100000
            
            if (x, y) in seen:
                if dp[x][y] > 0:
                    return dp[x][y]
                else:
                    return 100000
            
            if mat[x][y] == 0:
                return 0
            
            else:
                seen.add((x, y))
                dp[x][y] = min(dfs(x+1, y)+1, dfs(x-1, y)+1, dfs(x, y+1)+1, dfs(x, y-1)+1)
                return dp[x][y]
                    
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and dp[i][j] < 1:
                    dfs(i, j)
                print(dp)
                    
                    
        return dp
        """

       