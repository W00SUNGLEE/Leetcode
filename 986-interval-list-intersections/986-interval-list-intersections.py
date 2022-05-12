class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        
        i = 0
        j = 0
        
        while i < len(firstList) and j < len(secondList):
            
            if firstList[i][0] > secondList[j][1]:
                j += 1
                continue
                
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
                
            tmp = []
            tmp.append(max(firstList[i][0], secondList[j][0]))
                
            if firstList[i][1] < secondList[j][1]:
                tmp.append(firstList[i][1])
                i += 1
                    
            elif firstList[i][1] > secondList[j][1]:
                tmp.append(secondList[j][1])
                j += 1
                    
            else: #firstList[i][1] == secondList[j][1]:
                tmp.append(firstList[i][1])
                i += 1
                j += 1
                    
            answer.append(tmp)
                
        return answer