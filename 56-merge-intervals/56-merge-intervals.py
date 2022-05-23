class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        answer = []
        
        if len(intervals) == 0:
            return answer
        
        intervals.sort()
        
        answer.append(intervals[0])
        
        for i in range(1, len(intervals)):
            answerEnd = len(answer) - 1
            
            if intervals[i][0] <= answer[answerEnd][1]:
                if intervals[i][1] >= answer[answerEnd][1]:
                    answer[answerEnd][1] = intervals[i][1]
                    
                else:
                    continue
                
            else:
                answer.append(intervals[i])
                
        print(answer)
        return answer