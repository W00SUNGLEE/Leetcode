class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        solution = []
        
        tmp = [0]
        
        check = [0] * (n+1)
        
        def comb(v):
            if v == k:
                solution.append([tmp[i] for i in range(1,len(tmp))])
                
            else:
                for i in range(1, n+1):
                    if i not in tmp and i > tmp[len(tmp)-1]:
                        tmp.append(i)
                        comb(v+1)
                        tmp.pop()
        
        comb(0)
        
        return solution
                        
                    