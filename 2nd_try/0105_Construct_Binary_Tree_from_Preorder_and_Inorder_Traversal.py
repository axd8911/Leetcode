# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {val:i for i,val in enumerate(inorder)}
        def helper(l,r):
            if l < r:
                root = TreeNode(preorder.pop(0))
                split = dic[root.val]
                root.left = helper(l,split)
                root.right = helper(split+1,r)
                return root

        return helper(0,len(preorder))
