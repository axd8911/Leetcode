# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # if it is smaller than its prev
        # if first found, it prev is the large number
        # if second found, itself is the small number

        large = None
        small = None
        past = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if past and root.val<past.val:
                if not large:
                    large = past
                    small = root
                if large:
                    small = root

            past = root
            root = root.right

        large.val, small.val = small.val, large.val
        return root
