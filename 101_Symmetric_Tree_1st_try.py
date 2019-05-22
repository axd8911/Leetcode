'''
99.46%
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        self.result = True
        
        root2 = root
        
        def compare(root1, root2):
            
            if root1 and root2 == None:
                self.result = False
                return
            if root2 and root1 == None:
                self.result = False
                return
            if root1 and root2 and root1.val != root2.val:
                self.result = False
                return
            
            if root1 and root2:
                compare(root1.left,root2.right)
                compare(root1.right,root2.left)
                
        if root or root2:
            compare(root,root2)
        return self.result
        
