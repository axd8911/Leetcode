# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        result = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return result

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            save = curr.next.next
            new = curr.next
            new.next = head
            curr.next = save
            head = new
        return head
