class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        List = []
        tmp_List = []
        
        
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    cnt += 1
            tmp_List.append(cnt)
        
        
        K_count = 0
        for i in range(len(mat[0])+1):
            if K_count == k:
                    break
            
            for j in range(len(tmp_List)):
                if tmp_List[j] == i:
                    List.append(j)
                    K_count += 1
                if K_count == k:
                    break
                    
        return List
                