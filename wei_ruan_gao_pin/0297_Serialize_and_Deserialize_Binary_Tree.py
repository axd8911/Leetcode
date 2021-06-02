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
            return 'N'
        output = [str(root.val)]
        curr = collections.deque([root])
        while curr:
            temp=curr.popleft()
            if temp.left:
                output.append(str(temp.left.val))
                curr.append(temp.left)
            else:
                output.append('N')
            if temp.right:
                output.append(str(temp.right.val))
                curr.append(temp.right)
            else:
                output.append('N')                    
                
        print (output)
        return ' '.join(output)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'N':
            return None
        
        data = data.split(' ')
        idx = 0
        root = TreeNode(data[0])
        curr = collections.deque([root])
        while curr:
            temp = curr.popleft()
            idx +=1
            if data[idx]=='N':
                temp.left = None
            else:
                node = TreeNode(int(data[idx]))
                temp.left = node
                curr.append(node)
            idx +=1
            if data[idx]=='N':
                temp.right = None
            else:
                node = TreeNode(int(data[idx]))
                temp.right = node
                curr.append(node)
        return root
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
