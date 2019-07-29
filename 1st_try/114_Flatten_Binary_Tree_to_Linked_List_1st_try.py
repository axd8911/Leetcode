'''
97.82%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.output = TreeNode(None)
        
        def dp(root):
            if root:
                left = root.left
                right = root.right
                self.output.left = None
                self.output.right = root
                self.output = self.output.right
                self.output.right = dp(left)
                self.output.right = dp(right)
            
        if root:
            dp(root)
            
        return root
