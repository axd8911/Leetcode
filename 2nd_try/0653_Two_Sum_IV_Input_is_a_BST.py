# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        exist = set()

        queue = collections.deque([root])
        while queue:

            curr = queue.pop()
            if k-curr.val in exist:
                return True
            exist.add(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return False
