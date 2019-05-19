'''
99.59%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = small2 = ListNode(None)
        large = large2 = ListNode(None)
        
        
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        small.next = None
        large.next = None
        small.next = large2.next
        return small2.next
                
