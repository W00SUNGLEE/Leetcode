import sys

class Solution:
    def findMin(self, nums: List[int]) -> int:
                
        start = 0
        end = len(nums)-1
        answer = [sys.maxsize]
        
        def rotatedBinarySearch(start, end):
            
            if start > end:
                return
            
            mid = (start+end) // 2
            if answer[0] > nums[mid]:
                answer[0] = nums[mid]
            
            if nums[start] <= nums[end]:
                if answer[0] > nums[start]:
                    answer[0] = nums[start]
                    print(answer[0])
                
            else: #nums[start] > nums[end]
                rotatedBinarySearch(start, mid-1)
                rotatedBinarySearch(mid+1, end)
            
            return
        
        rotatedBinarySearch(start, end)
        return answer[0]