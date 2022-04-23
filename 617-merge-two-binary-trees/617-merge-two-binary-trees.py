# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            root1.val = root1.val + root2.val
            
            #left
            if root2.left != None:
                if root1.left == None:
                    root1.left = root2.left
            
                else: #root1.left != None
                    dfs(root1.left, root2.left)
            
            #right
            if root2.right != None:
                if root1.right == None:
                    root1.right = root2.right
                
                else: #root1.right != None
                    dfs(root1.right, root2.right)
                    
        if root1 == None and root2 == None:
            return None
        
        elif root1 == None and root2 != None:
            return root2
        
        elif root1 != None and root2 == None:
            return root1
        
        else: #root1 != None and root2 != None
            dfs(root1, root2)
            return root1