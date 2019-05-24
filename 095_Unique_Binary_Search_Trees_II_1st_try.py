# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        # Each number should be in root
        # Smaller number should go to its left, and bigger number should go to its right
        # Smaller number and biger number set each repeat the same
        
        if n == 0:
            return []
        
        def dfs(start,end):
            if start > end:
                return [None]
            result = []
            for i in range(start,end+1):
                left = dfs(start,i-1)
                right = dfs(i+1,end)
                
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        result.append(root)
            return result
        if n:
            output = dfs(1,n)
                        
        return output
