class Solution:
    def tribonacci(self, n: int) -> int:
        tri_array = [0, 1, 1]
        
        if n == 0:
            return 0
        
        elif n == 1:
            return 1
        
        elif n == 2:
            return 1
        
        else:
            for i in range(3,n):
                tri_array.append(tri_array[i-3] + tri_array[i-2] + tri_array[i-1])
            return tri_array[n-3] + tri_array[n-2] + tri_array[n-1]
        