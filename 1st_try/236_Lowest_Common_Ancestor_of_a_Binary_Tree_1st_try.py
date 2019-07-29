'''
95%
Although it seems that I understood the solution, it is still important to come back and check about the algorithm.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 有趣且重要的逻辑：两人共同的最晚先祖，那么这两人必在该先祖处分叉，或者一个是该先祖本尊
# 必须是左边一个孩子（True），右边一个孩子（True），或者其中一个孩子是自己
# 再往上一辈，所求的两个孩子都在那个先祖一边了，不符合条件

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.answer = None
        
        def dp(root):
            if not root:
                return False
            left = dp(root.left)
            right = dp(root.right)
            
            own = root == p or root == q
            if left + right + own >= 2:
                self.answer = root
                
            return left or right or own
        
        dp(root)
        return self.answer
