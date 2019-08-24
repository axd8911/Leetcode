# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root,minL,maxR):
            if not root:
                return True
            if root.val >= maxR or root.val <= minL:
                return False
            return helper(root.left,minL,root.val) and helper(root.right,root.val,maxR)
        return helper(root,float('-inf'),float('inf'))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True
