'''
99.6%

'''


#Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
                    
#Iteration
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        level = 0
        
        allItem = [root]
        n = 0
        
        while allItem != [None for i in range(len(allItem))]:
            new = []
            for item in allItem:
                if item != None:
                    new.append(item.left)
                    new.append(item.right)
            allItem = new
            n = n + 1
            
        return n
            
                    
        
