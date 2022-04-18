class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1
        
        start = 0
        end = m
        
        while start <= end:
            mid = (start+end)//2
            
            if target < matrix[mid][0]:
                end = mid-1
                
            elif target > matrix[mid][n]:
                start = mid+1
                
            else: #target >= matrix[mid][0] and target <= matrix[mid][n]
                start = 0
                end = n
                
                while start <= end:
                    mid2 = (start+end)//2
                
                    if target < matrix[mid][mid2]:
                        end = mid2-1
                
                    elif target > matrix[mid][mid2]:
                        start = mid2+1
                        
                    else: #target == matrix[mid][mid2]
                        return True

                return False
            
        return False