class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        x, y = 0, 0
        
        new_mat = []
        
        
        
        print(new_mat)
        
        for i in range(len(mat)):
            for data in mat[i]:
                if y == 0:
                    new_mat.append([])
                    
                new_mat[x].append(data)
                
                if y < c-1:
                    y += 1
                    
                else: #y == c
                    x += 1
                    y = 0
                    
        return new_mat
            