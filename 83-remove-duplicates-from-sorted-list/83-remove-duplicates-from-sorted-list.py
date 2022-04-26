# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preNode = None
        tmp = 1000
        start = head
        while head:
            if head.val == tmp:
                preNode.next = head.next
                head = head.next
                continue
            
            tmp = head.val
            preNode = head
            head = head.next
            
        return start
            
            