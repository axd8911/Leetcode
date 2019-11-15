# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = move = ListNode(0)

        while l1 or l2 or carry:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)

            curr = l1.val + l2.val + carry
            stay = curr%10
            carry = curr//10
            move.next = ListNode(stay)
            move = move.next
            l1 = l1.next
            l2 = l2.next


        return res.next
