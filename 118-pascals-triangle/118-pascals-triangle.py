class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        else:
            solution = [[0 for _ in range(i+1)] for i in range(numRows)]
            solution[0][0] = 1
            
            for i in range(numRows-1):
                for j in range(i+1):
                    solution[i+1][j] += solution[i][j]
                    solution[i+1][j+1] += solution[i][j]
                    
            return solution