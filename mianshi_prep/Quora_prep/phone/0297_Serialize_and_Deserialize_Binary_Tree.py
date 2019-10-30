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
        # if there is a node, its left and right both should take a place even when both are None
        #print (root)
        if not root:
            return []
        output = [root.val]
        curr = collections.deque([root])
        while curr:
            length = len(curr)
            for i in range(len(curr)):
                item = curr.popleft()
                if item:
                    if item.left:
                        output.append(item.left.val)
                        curr.append(item.left)
                    else:
                        output.append(None)
                    if item.right:
                        output.append(item.right.val)
                        curr.append(item.right)
                    else:
                        output.append(None)
        #print (output)
        return output



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return

        data = collections.deque(data)
        curr = data.popleft()
        root = TreeNode(curr)
        row = [root]
        while row:
            new = []
            for i in range(len(row)):
                item1 = data.popleft()
                item2 = data.popleft()

                if item1 != None:
                    node1 = TreeNode(item1)
                    new.append(node1)
                    row[i].left = node1

                if item2 != None:
                    node2 = TreeNode(item2)
                    new.append(node2)
                    row[i].right = node2

            row = new
        #print (root)
        return root




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
