'''
70%
Make some good use of 'or' in variable assigning.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        backup = root
        
        while root:
            curr = None
            start = None
            while root:
                
                if root.left and root.right:
                    root.left.next = root.right                
                if curr == None:
                    start = root.left or root.right
                if root.right or root.left:
                    curr = root.right or root.left

                if root.next and curr and (root.next.left or root.next.right):
                    curr.next = root.next.left or root.next.right
                        
                #elif not root.next and curr:
                #    curr.next = None
                root = root.next
            root = start
        
        return backup
                    
