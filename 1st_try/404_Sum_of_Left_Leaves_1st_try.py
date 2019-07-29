'''
99.88%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.total = 0
        
        def dp(root):
            if not root:
                return 
            
            dp(root.left)
            if root.left and not root.left.left and not root.left.right:
                
                self.total = self.total + root.left.val
            dp(root.right)
            
        if root:
            dp(root)
            
        return self.total
