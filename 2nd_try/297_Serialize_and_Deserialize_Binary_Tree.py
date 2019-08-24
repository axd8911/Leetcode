# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return []
        output = collections.deque([root.val])
        curr = collections.deque([root])
        while True:
            new = []
            for i in range(len(curr)):
                item = curr.popleft()
                if item:
                    if item.left:
                        curr.append(item.left)
                        new.append(item.left.val)
                    else:
                        curr.append(None)
                        new.append(None)
                    if item.right:
                        curr.append(item.right)
                        new.append(item.right.val)
                    else:
                        curr.append(None)
                        new.append(None)
            if new == [None]*len(new):
                break
            output.extend(new)
        return output

    def deserialize(self, data):
        if not data:
            return []
        output = TreeNode(data.popleft())
        curr = collections.deque([output])
        while data:
            for i in range(len(curr)):
                item = curr.popleft()
                l = TreeNode(data.popleft())
                r = TreeNode(data.popleft())
                if l.val != None:
                    item.left = l
                    curr.append(l)
                if r.val != None:
                    item.right = r
                    curr.append(r)

        return output













# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
