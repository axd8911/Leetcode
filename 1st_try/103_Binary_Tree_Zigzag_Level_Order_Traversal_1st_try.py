# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        
        node = [root]
        data = [[root.val]]
        n = 0
        
        while data[-1] != []:
            new = []
            data.append([])
            for item in node:                
                if item.left != None:
                    new.append(item.left)
                if item.right != None:
                    new.append(item.right)
            node = new
            if n%2 == 0:
                new = new[::-1]
            for item in new:
                data[-1].append(item.val)
            n = n + 1
        data.pop()
        return data
                
                
            
