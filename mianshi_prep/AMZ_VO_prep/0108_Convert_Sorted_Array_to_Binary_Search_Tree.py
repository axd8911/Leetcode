# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(l,r):
            if l>=r:
                return
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = helper(l,mid)
            node.right = helper(mid+1,r)

            return node

        return helper(0,len(nums))
