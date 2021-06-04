"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        backup = head
        while backup:
            new = Node(backup.val)
            new.next = backup.next
            backup.next = new
            backup = backup.next.next
        backup = head
        while backup:
            if backup.random:
                backup.next.random = backup.random.next
            backup = backup.next.next
        backup = head
        curr = res = Node(0)
        while backup:
            curr.next = backup.next
            curr = curr.next
            backup = backup.next.next
        return res.next
