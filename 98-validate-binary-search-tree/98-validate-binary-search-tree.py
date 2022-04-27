# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        
        def valid(node, preMin, preMax) -> bool:
            if node == None:
                return True
            
            else:
                if preMin < node.val < preMax:
                    return valid(node.left, preMin, node.val) and valid(node.right, node.val, preMax)
                    
                else:
                    return False
                
            """
            else:
                if node.left == None:
                    validLeft = True
                else:
                    if node.left.val < node.val:
                        validLeft = valid(node.left)
                    else:
                        validLeft = False
            
                if node.right == None:
                    validRight = True
                else:
                    if node.right.val > node.val and:
                        validRight = valid(node.right)
                    else:
                        validRight = False
                print(validLeft, validRight)
                
                return validLeft and validRight
                """
        
        return valid(root, -sys.maxsize-1, sys.maxsize)