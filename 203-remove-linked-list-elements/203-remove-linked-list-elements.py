# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        preNode = None
        node = head
        
        while node:
            if node.val == val:
                if preNode == None:
                    head = head.next
                else:
                    preNode.next = node.next
            else:
                preNode = node
            node = node.next
        
        return head