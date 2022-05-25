from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n  = len(matrix)
        for j in range(n//2):
            
            for i in range(j,n-1-j):
                
                tmp1 = matrix[j][i]
            
                tmp2 = matrix[i][n-1-j]
                matrix[i][n-1-j] = tmp1
            
                tmp1 = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = tmp2
            
                tmp2 = matrix[n-1-i][j]
                matrix[n-1-i][j] = tmp1
            
                matrix[j][i] = tmp2
            
            
            
            
            
            
            
            
            
            
            
            """
            tmp1 = matrix[0][i]
            
            tmp2 = matrix[i][n-1]
            matrix[i][n-1] = tmp1
            
            tmp1 = matrix[n-1][n-1-i]
            matrix[n-1][n-1-i] = tmp2
            
            tmp2 = matrix[n-1-i][0]
            matrix[n-1-i][0] = tmp1
            
            matrix[0][i] = tmp2
            """
               
        """
        deq = deque([deque(x) for x in matrix])
        
        tmpZ = deque()
        tmpN = deque()
        
        for i in range(n):
            tmpZ.appendleft(deq[i].popleft())
            tmpN.appendleft(deq[i].pop())
            
        tmp1 = deq.popleft()
        tmp2 = deq.pop()
        
        deq.append(tmpZ)
        deq.appendleft(tmpN)
        
        for i in range(1,n-1):
            deq[i].append(tmp1.popleft())
            deq[i].appendleft(tmp2.popleft())
        print(deq)
        print(matrix)
        """