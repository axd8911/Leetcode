# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        addup = 0
        output1 = output2 = ListNode(0)

        while l1 and l2:
            if l1.next and not l2.next:
                l2.next = ListNode(0)
            elif not l1.next and l2.next:
                l1.next = ListNode(0)

            curr = l1.val + l2.val + addup
            output1.next = ListNode((curr)%10)
            addup = curr//10
            output1,l1,l2 = output1.next,l1.next,l2.next

        if addup:
            output1.next = ListNode(addup)
        return output2.next
