class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        solution = []
        
        tmp = []
        
        def comb(v, index):
            if v == k:
                solution.append([i for i in tmp])
                
            else:
                for i in range(index+1, n+1):
                    if i not in tmp:
                        tmp.append(i)
                        comb(v+1, i)
                        tmp.pop()
        
        comb(0, 0)
        
        return solution
                        
                    