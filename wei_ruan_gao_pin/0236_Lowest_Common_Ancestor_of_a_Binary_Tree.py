# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        
        def getResult(node):
            if node == None:
                return False
            left = getResult(node.left)
            right = getResult(node.right)
            
            curr = node == p or node == q
            
            if curr + left + right >=2:
                self.result = node
                
            return curr or left or right
        
        getResult(root)
        return self.result
