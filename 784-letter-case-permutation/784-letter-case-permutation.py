class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        solution = []
        
        tmp = []
        
        def backtracking(v):
            if v == len(s):
                solution.append("".join([i for i in tmp]))
                                
            else:
                if s[v].isalpha():
                    tmp.append(s[v].lower())
                    backtracking(v+1)
                    tmp.pop()
                    
                    tmp.append(s[v].upper())
                    backtracking(v+1)
                    tmp.pop()
                                
                                
                else:
                    tmp.append(s[v])
                    backtracking(v+1)
                    tmp.pop()
                                
        backtracking(0)
                                
        return solution