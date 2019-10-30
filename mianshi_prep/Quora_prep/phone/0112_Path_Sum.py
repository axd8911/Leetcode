# iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []

        while stack or root:
            while root:
                sum -= root.val
                stack.append((root,sum))
                root = root.left
            root,sum = stack.pop()
            if not root.left and not root.right and sum == 0:
                    return True
            root = root.right
        return False

# recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
