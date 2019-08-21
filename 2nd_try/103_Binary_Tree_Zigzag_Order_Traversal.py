# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []

        curr = [root]

        while curr:
            new = []
            output.append([])
            for item in curr:
                output[-1].append(item.val)
                if item.left:
                    new.append(item.left)
                if item.right:
                    new.append(item.right)
            curr = new

        for i in range(1,len(output),2):
            output[i] = output[i][::-1]

        return output
