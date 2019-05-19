'''
98.15%
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        head2 = head

        while head2.next:
            if head2.val == head2.next.val:
                head2.next = head2.next.next
            else:
                head2 = head2.next
        
        
        return head
        
