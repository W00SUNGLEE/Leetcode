class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        
        while index1 < index2:
            if  numbers[index1] + numbers[index2] < target:
                index1 += 1
                
            elif numbers[index1] + numbers[index2] == target:
                return [index1+1, index2+1]
            
            else: #numbers[index1] + numbers[index2] > target
                index2 -= 1
                
                
        return -1
            
        
        
        """
        distinct = [numbers[0], numbers[1]]
        for i in range(2, len(numbers)):
            if numbers[i] == distinct[i-1] and numbers[i] == distinct[i-2]:
                continue
            distinct.append(numbers[i])
        
        print(distinct)
        """
        """
        distinct = list(set(numbers))
        
        print(distinct)
        
        for i in range(len(distinct)):
            for j in range(i, len(distinct)):
                if distinct[i] + distinct[j] == target:
                    x_index = i
                    y_index = j
        """
        
        """
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):  
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        """
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        
        return -1