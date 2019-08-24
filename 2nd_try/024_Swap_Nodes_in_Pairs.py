# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        curr = output = ListNode(0)
        curr.next = head
        while curr.next and curr.next.next:
            old = curr
            curr = curr.next
            save = curr.next.next
            new = curr.next
            new.next = curr
            old.next = new
            curr.next = save
        return output.next
