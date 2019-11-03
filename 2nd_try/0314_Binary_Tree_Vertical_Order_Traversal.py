# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        dic = collections.defaultdict(list)

        def helper(root,idx,line):
            if not root:
                return
            dic[idx].append((root,line))

            line += 1
            helper(root.left,idx-1,line)
            helper(root.right,idx+1,line)
            line -= 1

        helper(root,0,0)
        myKey = sorted(list(dic.keys()))

        res = []

        for item in myKey:
            res.append([])
            for node,line in dic[item]:
                res[-1].append((node.val,line))

        for i in range(len(res)):
            res[i].sort(key = lambda x:x[1])
            res[i] = [item[0] for item in res[i]]

        return res
