class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        answer = [-1]
        
        def rotatedBinarySearch(start, end):
            
            if start > end:
                return
            
            mid = (start+end) // 2
                
            if nums[mid] == target:
                answer[0] = mid
                    
            else:
                if nums[start] < nums[end]:
                    if nums[mid] > target:
                        rotatedBinarySearch(start, mid-1)
                    if nums[mid] < target:
                        rotatedBinarySearch(mid+1, end)
                
                else: #nums[start] > nums[end]
                    rotatedBinarySearch(start, mid-1)
                    rotatedBinarySearch(mid+1, end)
            
            return
        
        rotatedBinarySearch(start, end)
        return answer[0]