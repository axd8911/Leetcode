# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        node = [root]
        data = []
        data.append([root.val])
        
        while data[-1] != []:
            new = []
            for item in node:
                if item != None:
                    new.append(item.left)
                    new.append(item.right)
            data.append([])
            for item in new:
                if item != None:
                    data[-1].append(item.val)
            node = new
        data.pop()    
        return data
