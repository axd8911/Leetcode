# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = output = ListNode(0)
        curr.next = head
        backupK = k

        while head:
            stepper = old = curr
            cap = curr = curr.next
            while k:
                stepper = stepper.next
                if not stepper:
                    return output.next
                k-=1
            k = backupK

            while curr and curr.next and k>1:
                k-=1
                new = curr.next         # location next node to go front
                save = curr.next.next   #store the nodes after
                new.next = cap          #lift new before cap
                cap = new               #now new is the new cap
                curr.next = save        # relink the saved nodes
                old.next = cap
            k = backupK
            
