# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def recursion(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                self.count += 1
            currMax = max(currMax, node.val)
            recursion(node.left,currMax)
            recursion(node.right,currMax)
        
        recursion(root,root.val)
        return self.count
