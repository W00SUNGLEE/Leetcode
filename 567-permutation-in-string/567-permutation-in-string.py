from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0 
        end = start + len(s1) - 1
        
        dic_s1 = defaultdict(int)
        dic_s2 = defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            dic_s1[s1[i]] += 1
            dic_s2[s2[i]] += 1
        
        if Solution.equal_dic(self, dic_s1, dic_s2):
            return True
        
        
        #start = 1
        #while start < len(s2) - len(s1) + 1:

        for i in range(len(s1),len(s2)):
            dic_s2[s2[i - len(s1)]] -= 1
            dic_s2[s2[i]] += 1
                   
            if Solution.equal_dic(self, dic_s1, dic_s2):
                return True
        
        return False
    
    def equal_dic(self, dic_s1: dict, dic_s2: dict) -> bool:
        for key in dic_s1.keys():
            if dic_s1[key] != dic_s2[key]:
                return False
            
        return True    