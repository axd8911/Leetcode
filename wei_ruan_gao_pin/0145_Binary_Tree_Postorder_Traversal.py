# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        allNodes = []
        res = []
        while allNodes or root:
            while root:
                res.append(root.val)
                allNodes.append(root)
                root = root.right
            root = allNodes.pop()
            root = root.left
        return res[::-1]
