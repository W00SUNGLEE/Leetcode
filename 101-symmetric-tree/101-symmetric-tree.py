# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(nodeLeft, nodeRight) -> bool:
            if nodeLeft == None and nodeRight == None:
                return True
            
            elif nodeLeft != None and  nodeRight == None:
                return False
                
            elif nodeLeft == None and  nodeRight != None:
                return False
            
            else: #nodeLeft != None and  nodeRight != None
                if nodeLeft.val == nodeRight.val:                    
                    return dfs(nodeLeft.left, nodeRight.right) and dfs(nodeLeft.right, nodeRight.left)
                
                else: #nodeLeft.val != nodeRight.val
                    return False
                
        return dfs(root.left, root.right)