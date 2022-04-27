# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val, None, None)
        
        def insert(node, val):
            if val < node.val:
                if node.left == None:
                    node.left = TreeNode(val, None, None)
                else:
                    insert(node.left, val)
                
            else: #val > node.val
                if node.right == None:
                    node.right = TreeNode(val, None, None)
                else:
                    insert(node.right, val)
            
        
        insert(root, val)
        
        return root