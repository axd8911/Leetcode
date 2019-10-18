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
        res = curr = Node(0,None,None)

        dic = {}
        stack = []

        while head:
            if head.val not in dic:
                curr.next = Node(head.val,None,None)
                dic[head.val] = curr.next
            else:
                curr.next = dic[head.val]

            if head.random:
                if head.random.val not in dic:
                    curr.next.random = Node(head.random.val,None,None)
                    dic[head.random.val] = curr.next.random
                else:
                    curr.next.random = dic[head.random.val]
            head = head.next
            curr = curr.next
        return res.next
            
