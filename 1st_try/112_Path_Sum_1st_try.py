# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        self.judge = False
        
        def sumup(root,total):

            if not root:
                return
            curr = root.val
            total = total + curr
            
            sumup(root.left,total) or sumup(root.right,total)
            
            if total == sum and not root.left and not root.right:
                self.judge = True            
            
        if root:
            sumup(root,0)
            
        return self.judge
