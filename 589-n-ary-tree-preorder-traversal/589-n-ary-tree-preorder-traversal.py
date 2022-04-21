"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:   
        arr = []
        
        if root == None:
            return arr
        else:
            Solution.dfs(self, root, arr)
            return arr
    
    def dfs(self, node: 'Node', arr: List[int]):
        arr.append(node.val)
        
        for child in node.children:
            self.dfs(child, arr)
        