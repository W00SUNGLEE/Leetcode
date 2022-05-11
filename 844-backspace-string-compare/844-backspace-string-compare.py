class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        
        while i >= 0 or j >= 0:
            if i >= 0 and s[i] == "#":
                i -= 1
                cnt = 1
                while i >= 0 and cnt > 0:
                    if s[i] != "#":
                        cnt -= 1

                    else: #s[i] == "#"
                        cnt += 1
                        
                    i -= 1

                continue
                
            if j >= 0 and t[j] == "#":
                j -= 1
                cnt = 1
                while j >= 0 and cnt > 0:
                    if t[j] != "#":
                        cnt -= 1
                        
                    else: #t[i] == "#"
                        cnt += 1
                        
                    j -= 1

                continue
            
            print(s[i], t[j])
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    print(1)
                    return False
            else:
                return False
            
            i -= 1
            j -= 1
            
        if i <= -1 and j <= -1:
            return True
        
        else:
            print(2)
            return False