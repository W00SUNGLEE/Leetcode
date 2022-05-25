class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [0 for _ in range(rowIndex+1)]
        answer[0] = 1
        
        for i in range(1, rowIndex+1):
            
            tmp_answer = [0 for _ in range(i+1)]
            
            for j in range(i):
                tmp_answer[j] += answer[j]
                tmp_answer[j+1] += answer[j]
                
            answer = tmp_answer
            
        return answer
            