# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        cnt = 0
          
        while node != None:
            cnt += 1
            node = node.next
        
        node = head
        
        if cnt == n:
            return head.next
        
        for i in range(cnt-n-1):
            node = node.next
        
        if node == head:
            if node.next == None:
                head = None
            else:
                node.next = node.next.next
        
        else:
            node.next = node.next.next   
            
        return head
    
        