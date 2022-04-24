"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        
        queue = deque([])
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        
        tmp = root
    
        while queue:
            node = queue.popleft()
            tmp.next = node
            tmp = node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        node = root
        while node != None:
            node.next = None
            node = node.right
            
        return root

"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        
        queue = []
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)
        
        tmp = root
    
        while queue:
            node = queue.pop(0)
            tmp.next = node
            tmp = node
            
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        
        node = root
        while node != None:
            node.next = None
            node = node.right
            
        return root
"""