"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        stack =[]

        while curr or stack:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child = None
                curr.next.prev = curr
            if stack and not curr.next:
                new = stack.pop()
                curr.next = new
                new.prev = curr
            curr = curr.next         
        return head
