'''
99.73%
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        found = False
        nodes = [root]
        n = 1
        while True:
            new = []
            for item in nodes:
                if item.left == None and item.right == None:
                    found = True
                    break
                if item.left:
                    new.append(item.left)
                if item.right:
                    new.append(item.right)
                
            if found == True:
                break
            nodes = new                
            n = n + 1
        return n
