class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = str(n)
        
        product_digit = 1
        sum_digit = 0
        for i in range(len(arr)):
            product_digit *= int(arr[i])
            sum_digit += int(arr[i])
            
        return product_digit - sum_digit