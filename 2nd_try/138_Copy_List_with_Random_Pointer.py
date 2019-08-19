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

        output = curr = Node(0,None,None)
        exist = {}
        while head:
            if head.val not in exist:
                curr.next = Node(head.val,None,None)
                exist[head.val] = curr.next
            else:
                curr.next = exist[head.val]
            if head.random:
                if head.random.val not in exist:
                    curr.next.random = Node(head.random.val,None,None)
                    exist[head.random.val] = curr.next.random
                else:
                    curr.next.random = exist[head.random.val]
            if head.next:
                if head.next.val not in exist:
                    curr.next.next = Node(head.next.val,None,None)
                    exist[head.next.val] = curr.next.next
                else:
                    curr.next.next = exist[head.next.val]
            curr = curr.next
            head = head.next
        return output.next
