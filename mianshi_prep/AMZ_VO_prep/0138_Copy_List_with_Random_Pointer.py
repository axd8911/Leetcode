"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        res = curr = Node(0,None,None)
        curr.next = head

        while head:
            if head:
                if head not in dic:
                    dic[head] = Node(head.val,None,None)
                curr.next = dic[head]

            if head.random:
                if head.random not in dic:
                    dic[head.random] = Node(head.random.val,None,None)
                curr.next.random = dic[head.random]

            head = head.next
            curr = curr.next

        return res.next
