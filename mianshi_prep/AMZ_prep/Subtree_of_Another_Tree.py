# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def helper(root):
            if root:
                return '!' + helper(root.left) +str(root.val) +  helper(root.right)
            else:
                return '@'

        str_s = helper(s)
        str_t = helper(t)
        print (str_s,str_t)

        if str_t in str_s:
            return True
        return False
