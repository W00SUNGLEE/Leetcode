# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        answer = True
        arr = []
        tmp = head
        
        
        while(tmp != None):
            #print(tmp.val)
            arr.append(tmp.val)
            tmp = tmp.next
        
        
        for i in range(0,len(arr)//2):
            if arr[i] != arr[-1-i]:
                answer = False
                
                
        return answer
        