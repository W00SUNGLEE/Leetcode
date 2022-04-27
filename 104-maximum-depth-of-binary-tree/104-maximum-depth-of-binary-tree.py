# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        queue = []
        solution = 0
        queue.append((root,1))
        
        while queue:
            node, depth = queue.pop(0)
            
            if node == None:
                solution = max(solution, depth-1)
                continue
                
            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))
        
        return solution