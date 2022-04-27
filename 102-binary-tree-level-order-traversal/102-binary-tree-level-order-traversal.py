# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        queue = []
        solution = []
        queue.append((root, 1))
        
        while queue:
            node, level = queue.pop(0)

            if len(solution) < level:
                solution.append([node.val])
            
            else:
                solution[level-1].append(node.val)
            
            if node.left != None:
                queue.append((node.left, level+1))
            if node.right != None:
                queue.append((node.right, level+1))
                
        return solution