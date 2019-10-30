#iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        stack = []
        combine = []
        res = []
        while root or stack:
            while root:
                sum -= root.val
                combine += [root.val]
                stack.append((root,combine[:],sum))
                root = root.left
            root,combine,sum = stack.pop()
            if not root.left and not root.right:
                if sum == 0:
                    res.append(combine[:])
            root = root.right

        return res

#recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res = []

        def dfs(root, combine, total):

            if not root:
                return

            if not root.left and not root.right and total == sum:
                res.append(combine)

            if root.left:
                dfs(root.left,combine+[root.left.val],total + root.left.val)
            if root.right:
                dfs(root.right,combine+[root.right.val],total + root.right.val)

        if root:
            dfs(root,[root.val],root.val)
        return res
