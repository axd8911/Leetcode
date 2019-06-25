# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        eachRow = [[root]]
        
        while eachRow[-1]:
            eachRow.append([])
            for item in eachRow[-2]:
                if item.left:
                    eachRow[-1].append(item.left)
                if item.right:
                    eachRow[-1].append(item.right)
        
        eachRow.pop()
        return ([item[-1].val for item in eachRow])
        
        
