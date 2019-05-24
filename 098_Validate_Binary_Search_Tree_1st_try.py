'''
97.56%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # all numbers on root left are smaller, all numbers on root right are bigger
        
        self.list = []
        self.valid = True
        
        def dfs(root):
            if len(self.list) >= 2 and self.list[-1]<=self.list[-2]:
                self.valid = False
            if root:
                dfs(root.left)
                self.list.append(root.val)
                dfs(root.right)
            
        if root:
            dfs(root)
            
        return self.valid
            
