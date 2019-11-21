# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        def helper(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                helper(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                helper(root.right)
        helper(root)
        target = target.val
        curr = collections.deque([target])
        visited = {target}
        while K>0:
            K-=1
            length = len(curr)
            for i in range(length):
                temp = curr.popleft()
                for item in graph[temp]:
                    if item not in visited:
                        curr.append(item)
                        visited.add(item)
        return list(curr)
