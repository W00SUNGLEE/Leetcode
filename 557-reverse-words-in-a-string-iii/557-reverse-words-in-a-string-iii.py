class Solution:
    def reverseWords(self, s: str) -> str:
        tmp_s = s.split()
        print(tmp_s)
        
        for i in range(len(tmp_s)):
            tmp_s[i] = list(tmp_s[i])
            tmp_s[i].reverse() 
            tmp_s[i] = "".join(tmp_s[i])
            #tmp_s[i] = "".join(reversed(tmp_s[i]))
            
        return " ".join(tmp_s)
        