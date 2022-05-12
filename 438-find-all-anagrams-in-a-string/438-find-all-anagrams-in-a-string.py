from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        answer = []
        
        m = len(s)
        n = len(p)
    
        dictS = defaultdict(int)
        dictP = defaultdict(int)
         
        for i in range(len(p)):
            dictP[p[i]] += 1
            
        keys = dictP.keys()
            
        print(dictP)
        
        i = 0
        j = 0
        
        while i <= m-n and j < m:
            print(s[j], dictS, s[j] in keys)
            if s[j] in keys:
                dictS[s[j]] += 1
                if dictS[s[j]] <= dictP[s[j]]:
                    #if j-i+1 < n:
                    if j-i+1 == n:
                        answer.append(i)
                        dictS[s[i]] -= 1
                        i += 1
        
                else: #dictS[j] > dictP[j]:
                    while i <= m-n:
                        if s[i] in keys:
                            dictS[s[i]] -= 1
                        i += 1
                        
                        if dictS[s[j]] == dictP[s[j]]:
                            break
                            
            else:
                i = j+1
                dictS = defaultdict(int)
            j += 1
            
        print(answer)
        
        return answer
                    
        """
        for i in range(len(s)):
            if s[i] in keys:
                dictS[i] += 1
                if start == -1
                    start = i
                
                else:
                    if i-n+1 > start:
                        
                    
        """