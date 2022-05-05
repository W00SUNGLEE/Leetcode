# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1000, head)
        
        preNode = head
        node = head.next
        
        print(head.next)
        
        while node:
            if node.next == None:
                break
            
            else:
                if node.val == node.next.val:
                    while node.next and node.val == node.next.val:
                        node = node.next
                    preNode.next = node.next
            
                else: #node.val != node.next.val
                    preNode = node
                            
                node = node.next 
                
        print(head.next)
        
        return head.next