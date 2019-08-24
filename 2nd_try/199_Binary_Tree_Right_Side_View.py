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
        output = []
        curr = collections.deque([root])
        while curr:
            for i in range(len(curr)):
                item = curr.popleft()
                if item.left:
                    curr.append(item.left)
                if item.right:
                    curr.append(item.right)
            output.append(item.val)
        return output
