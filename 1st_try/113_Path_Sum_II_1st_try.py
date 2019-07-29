'''
99.47%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
 
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.output = []

        
        def dp(root, combine, temp):

            if temp == sum and root.left == None and root.right == None:
                self.output.append(combine)
                
            if root.left:
                dp(root.left, combine + [root.left.val], temp + root.left.val)
            if root.right:
                dp(root.right, combine + [root.right.val], temp + root.right.val)

            
        if root:
            dp(root,[root.val],root.val)
            
        return self.output
