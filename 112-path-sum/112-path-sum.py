# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, tmpSum) -> bool:
            if node == None:
                return False
            
            else:
                tmpSum += node.val
                if node.left == None and node.right == None:                
                    if tmpSum == targetSum:
                        return True
                    
                return dfs(node.left, tmpSum) or dfs(node.right, tmpSum)
            
        return dfs(root, 0)