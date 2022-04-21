class Solution:
    def isHappy(self, n: int) -> bool:     
        original_n = n
        check_n = []
        while n != 1:
            str_n = str(n)
            
            n = 0
            for i in range(len(str_n)):
                n += int(str_n[i]) ** 2
            
            for i in range(len(check_n)):
                if n == check_n[i]:
                    return False
                
            check_n.append(n)
            
        return True
            