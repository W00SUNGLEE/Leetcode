# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_node = head
        cnt = 0
        arr = []

        while tmp_node != None:
            cnt += 1
            tmp_node = tmp_node.next
            
        tmp_node = head
        for i in range(cnt//2):
            tmp_node = tmp_node.next

        return tmp_node
        