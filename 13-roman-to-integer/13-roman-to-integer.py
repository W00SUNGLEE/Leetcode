class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        
        i=0
        
        while(i < len(s)):
            M_count = 0
            
            if s[i] == 'M':
                M_count = 1
                C_count = 0
                
                for j in range(i+1, len(s)):
                    if s[j] == 'M':
                        M_count += 1
                    else:
                        break
                answer += M_count * 1000
                
                i += M_count
                continue
        
        
            if s[i] == 'D':
                answer += 500
                i += 1
                continue
            
            
            if s[i] == 'C':
                C_count = 1
                D_count = 0
                M_count = 0
                for j in range(i+1, len(s)):
                    if s[j] == 'C':
                        C_count += 1
                    elif s[j] == 'D':
                        D_count += 1
                        break
                    elif s[j] == 'M':
                        M_count += 1
                        break                        
                    else:
                        break
                        
                if D_count == 1:
                    answer += 400
                    i += C_count + D_count
                    continue
                elif M_count == 1:
                    answer += 900
                    i += C_count + M_count
                    continue
                else:
                    answer += C_count * 100
                    i += C_count
                    continue
            
            
            if s[i] == 'L':
                answer += 50
                i += 1
                continue
                
        
            if s[i] == 'X':
                X_count = 1
                L_count = 0
                C_count = 0
                for j in range(i+1, len(s)):
                    if s[j] == 'X':
                        X_count += 1
                    elif s[j] == 'L':
                        L_count += 1
                        break
                    elif s[j] == 'C':
                        C_count += 1
                        break                        
                    else:
                        break
                        
                if L_count == 1:
                    answer += 40
                    i += X_count + L_count
                    continue
                elif C_count == 1:
                    answer += 90
                    i += X_count + C_count
                    continue
                else:
                    answer += X_count * 10
                    i += X_count
                    continue
                    
                    
            if s[i] == 'V':
                answer += 5
                i += 1
                continue
            
            
            if s[i] == 'I':
                I_count = 1
                V_count = 0
                X_count = 0
                for j in range(i+1, len(s)):
                    if s[j] == 'I':
                        I_count += 1
                    elif s[j] == 'V':
                        V_count += 1
                        break
                    elif s[j] == 'X':
                        X_count += 1
                        break                        
                    else:
                        break
                        
                if V_count == 1:
                    answer += 4
                    i += I_count + V_count
                    continue
                elif X_count == 1:
                    answer += 9
                    i += I_count + X_count
                    continue
                else:
                    answer += I_count * 1
                    i += I_count
                    continue
 
        return answer