'''
97%
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.total = 0
        
        def dp(root,combine):
            if root and not root.left and not root.right:
                self.total = self.total + int(combine)
                return
            if root.left:
                dp(root.left,combine+str(root.left.val))
            if root.right:
                dp(root.right,combine+str(root.right.val))
            
        if root:
            dp(root,str(root.val))
            
        return self.total
