'''
96.57%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self,root):
        if root == None:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if abs(lh - rh) > 1:
            self.flag = True
        
        return 1 + max(lh,rh)
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        self.flag = False
        self.height(root)
        return not self.flag
        

            

        
        
