# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        res = [root.val]
        curr = collections.deque([root])

        while curr:
            for i in range(len(curr)):
                temp = curr.popleft()
                if temp.left:
                    curr.append(temp.left)
                    res.append(temp.left.val)
                else:
                    res.append(None)
                if temp.right:
                    curr.append(temp.right)
                    res.append(temp.right.val)
                else:
                    res.append(None)

        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = collections.deque(data)
        root = TreeNode(data.popleft())
        curr = collections.deque([root])
        while data:
            for i in range(len(curr)):
                temp = curr.popleft()
                n1 = data.popleft()
                n2 = data.popleft()
                if n1!= None:
                    temp.left = TreeNode(n1)
                    curr.append(temp.left)
                else:
                    temp.left = None
                if n2!=None:
                    temp.right = TreeNode(n2)
                    curr.append(temp.right)
                else:
                    temp.right = None
        return root




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
