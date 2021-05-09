# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        curr = head
        while curr and curr.next:
            save = curr.next.next
            toFront = curr.next
            toFront.next = head
            curr.next = save
            head = toFront
        return head
