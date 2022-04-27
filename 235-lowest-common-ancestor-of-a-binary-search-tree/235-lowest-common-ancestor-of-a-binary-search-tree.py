# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pVisted = []
        qVisted = []
        
        
        tmpVisited = []
        
        def dfs(node):
            if node == None:
                return 
            
            else:
                tmpVisited.append(node)
                
                if node.val == p.val:
                    for i in tmpVisited:
                        pVisted.append(i)
                    
                if node.val == q.val:
                    for i in tmpVisited:
                        qVisted.append(i)
                
                dfs(node.left)
                dfs(node.right)
                tmpVisited.pop()
            
            
        dfs(root)
        
        print(pVisted)
        print(qVisted)
        
        for p in reversed(pVisted):
            for q in reversed(qVisted):
                if p.val == q.val:
                    return p
        
                
        return None