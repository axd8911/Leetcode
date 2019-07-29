# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.output = None
        self.cnt = 0
        
        def dp(root):
            if not root:
                return 0
            
            result = 0
              
            result = dp(root.left) + 1
            self.cnt = self.cnt + 1
            if self.cnt == k:
                self.output = root.val
            result = dp(root.right) + 1
            
            return result
            
        if root:
            dp(root)
            
        return self.output
        
