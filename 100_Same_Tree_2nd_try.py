'''
97.7%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        self.output = True        
        def compare(p,q):
            
            if p and q == None:
                self.output = False
            if q and p == None:
                self.output = False
            if p and q and p.val != q.val:
                self.output = False
            if p and q:
                compare(p.left,q.left)
                compare(p.right,q.right)

        if p or q:
            output = compare(p,q)
            
        return self.output
            
        
        
