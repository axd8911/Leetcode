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

        curr = collections.deque([root])
        res =[]
        cnt = 0

        while curr:
            cnt += 1
            length = len(curr)
            thisLine = []
            for i in range(length):
                item = curr.popleft()
                thisLine.append(item.val)
                if item.left:
                    curr.append(item.left)
                if item.right:
                    curr.append(item.right)
            if cnt%2:
                res.append(thisLine)
            else:
                res.append(thisLine[::-1])

        return res
