import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = sys.maxsize
        second = sys.maxsize
        
        for num in nums:
            if num <= first:
                first = num
                
            elif num <= second:
                second = num
            
            else:
                return True
            
        return False
        
        """
        n = len(nums)
        
        first = nums[0]
        second = -sys.maxsize
        
        for i in range(1,n):
            if nums[i] < first:
                first = nums[i]

                
            elif nums[i] > first:
                if nums[i] < second:
                    second = nums[i]
                    
                elif nums[i] > second:
                    if second == -sys.maxsize:
                        second = nums[i]
                        
                    else:
                        return True
        
        return False
        """
            
            