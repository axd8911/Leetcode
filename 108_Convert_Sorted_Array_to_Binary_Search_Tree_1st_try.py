'''
99.37%
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return []
        
        def convert(dataSet):
            if dataSet == []:
                return
            
            loc = len(dataSet)//2
            left = dataSet[:loc]
            right = dataSet[loc+1:]
            root = TreeNode(dataSet[loc])
            root.left = convert(left)
            root.right = convert(right)
            
            return root
        
        if nums:
            result = convert(nums)
            
        return result
            
