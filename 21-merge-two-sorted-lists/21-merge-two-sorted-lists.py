# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = dummy = ListNode()
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else: # list1.val > list2.val
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
        
        """
        while list1 and list2:
            if list1.val <= list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
                
            else: #list1.val > list2.val
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
                
        
        if list1 or list2:
            tmp.next = list1 if list1 else list2
        
        return dummy.next
        """
        
        
        
        
        
        
        """
        if list1.val <= list2.val:
            node = ListNode(List1.val, None)
                
        else: #list1.val < list2.val
            node = List2
        """
        """
        def merge(list1, list2, node):
            if list1 == None and list2 == None:
                return None
            elif list1 != None and list2 == None:
                return list1
            elif list1 == None and list2 != None:
                return list2
            
            else: #list1 != None and list2 != None
                if list1.val <= list2.val:
                    if node == None:
                        merge(list1.next, list2, list1)
                        return list1
                    
                    else:
                        node.next = list1
                        merge(list1.next, list2, node.next)
                    
                        
                else: #list1.val > list2.val
                    if node == None:
                        merge(list1, list2.next, list2)
                        return list1
                    
                    else:
                        node.next = list1
                        merge(list1, list2.next, node.next)
        
        return merge(list1, list2, None)
        """