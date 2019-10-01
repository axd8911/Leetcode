# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = root.val
        def helper(root):
            if not root:
                return 0
            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            self.maximum = max(self.maximum,root.val+left+right)
            return root.val+max(left,right)
        helper(root)
        return self.maximum
