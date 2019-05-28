'''
92%

Do you want to do iteration layer by layer? Make some good use of the 'next' item in created linked list. 
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
               
        while root and root.left:
            
            root2 = root
            
            while root:
                
                root.left.next = root.right
                if root.next != None:
                    root.right.next = root.next.left
                else:
                    root.right.next = None
                
                root = root.next    
            root = root2
            root = root.left
        
        return backup

        
