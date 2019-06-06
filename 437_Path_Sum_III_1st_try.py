'''
50%
Should consider a better way to replace the list operation
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root跟各自的左右孩子们相加
# [10] --> [10,5],[5] --> 10,5,3  5,3  3
# 前序遍历，碰壁扣回

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.cnt = 0
        self.sumList = []
        
        def dp(root):
            
            for item in self.sumList:
                if item == sum:
                    self.cnt = self.cnt + 1
            if root:
                self.sumList = [item + root.val for item in self.sumList]
                self.sumList.append(root.val)

                dp(root.left)
                dp(root.right)

                self.sumList.pop()
                self.sumList = [item - root.val for item in self.sumList]
                
            
            
        if root:
            dp(root)
            
        return self.cnt // 2
            
