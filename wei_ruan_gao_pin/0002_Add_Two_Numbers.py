# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = mover = ListNode(0,None)
        position = 1
        while l1 or l2 or carry:
            if not l1:
                l1 = ListNode(0,None)
            if not l2:
                l2 = ListNode(0,None)
            curr = (l1.val+l2.val+carry)%10
            mover.next = ListNode(curr,None)
            carry = (l1.val+l2.val+carry)//10
            mover = mover.next
            l1 = l1.next
            l2 = l2.next

        return res.next
            
        
            
