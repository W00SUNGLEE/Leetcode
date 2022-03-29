class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_arr = [0 for _ in range(26)]
        magazine_arr = [0 for _ in range(26)]
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        for char in ransomNote:
            if char in alpha:
                ransomNote_arr[alpha.index(char)] += 1
                
        for char in magazine:
            if char in alpha:
                 magazine_arr[alpha.index(char)] += 1 
                    
        for i in range(26):
            if ransomNote_arr[i] > magazine_arr[i]:
                return False
            
        return True