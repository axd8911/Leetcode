'''
98.6%
'''
#Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        node = [root]
        
        while node:
            curr = node.pop()
            
            if curr:
                output.append(curr.val)
                node.append(curr.right)
                node.append(curr.left)
                
        return output

#recursion
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.output = []
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root:
            self.output.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            
        return self.output
