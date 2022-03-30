class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums)-1
        
        while head <= tail:
            index = (head+tail)//2 
            
            if nums[index] == target:
                return index
            elif nums[index] > target:
                tail = index - 1
            elif nums[index] < target:
                head = index + 1
                
        if nums[index] == target:
                return index 
        else:
            return -1