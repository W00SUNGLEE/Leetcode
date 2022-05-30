import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        first = nums[0]
        second = -sys.maxsize
        #third = nums[0]
        
        for i in range(1,n):
            print(first, second)
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
                
                
                """
                if nums[i] < second:
                    return True

                elif nums[i] > second:
                    if first == second:
                        second = nums[i]
                        
                    else:
                        return True
                        #third = nums[i]
                """
                    
                
            
            #if nums[i] < nums[i+1] < nums[i+2]:
                #print(nums[i], nums[i+1], nums[i+2])
                #return True
            
        return False
            
            