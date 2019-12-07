# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True

        def dfs(s,t):
            if not s and not t:
                return True
            if (not s and t) or (s and not t):
                return False
            return s.val == t.val and dfs(s.left,t.left) and dfs(s.right,t.right)


        def check(s,t):
            if not s:
                return False
            if dfs(s,t) == 1:
                return True

            return check(s.left,t) == 1 or check(s.right,t) == 1


        res = check(s,t)
        return res
