from collections import deque

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        move = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        
        answer = [[0 for _ in range(n)] for _ in range(n)]
        
        
        cnt = 0
        
        x = 0
        y = 0
        
        result = True
        
        while result:
            
            result = False
            
            cnt += 1
            answer[x][y] = cnt
            
            for i in range(4):
                xi, yi = move.popleft()
                newX = x + xi
                newY = y + yi
                
                if 0 <= newX < n and 0 <= newY < n and answer[newX][newY] == 0:
                    x = newX
                    y = newY
                    
                    move.appendleft((xi, yi))
                    result = True
                    break
                
                move.append((xi, yi))
                    
        return answer
        