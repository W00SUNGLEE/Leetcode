class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        print(nums)
        
        start = 0
        end = len(nums)-1
        
        if len(nums) == 1:
            return 0
        
        while start <= end:
            
            mid = (start+end) // 2
            
            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else: 
                    start = mid+1
            
            elif mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    end = mid-1
            
            else:
            
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
            
                elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                    start = mid+1
                
                elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
                    end = mid-1
                
                else:
                    end = mid-1
                
        
        return -1