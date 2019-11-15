# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:

        def left(node):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            if node.left:
                left(node.left)
            else:
                left(node.right)

        def right(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                right(node.right)
            else:
                right(node.left)
            boundary.append(node.val)

        def bottom(node):
            if not node:
                return
            bottom(node.left)
            if node != root and  not node.left and not node.right:
                boundary.append(node.val)
            bottom(node.right)

        if not root:
            return []
        boundary = [root.val]
        left(root.left)
        bottom(root)
        right(root.right)
        return boundary

        
