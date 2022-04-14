class Solution:
    def fib(self, n: int) -> int:
        fib_array = [0, 1]
        
        if n == 0:
            return 0
        
        elif n == 1:
            return 1
        
        else:
            for i in range(2, n+1):
                fib_array.append(fib_array[i-2]+fib_array[i-1])
            return fib_array[n]
            
            
            """
            if len(fib_array) > n:       
                return fib_array[n-2] + fib_array[n-1]
            elif len(fib_array) == n
                fib_array.append(fib_array[n-2] + fib_array[n-1])
                retrun fib_array[n]
            else:
                fib()
            """