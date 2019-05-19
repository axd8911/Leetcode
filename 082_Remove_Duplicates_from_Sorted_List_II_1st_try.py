'''
98.06%


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
        new2 = new = ListNode(None)
        repeat = None
    
        while head2.next:
            if head2.val == head2.next.val:
                repeat = head2.val
            if head2.val != head2.next.val and head2.val != repeat:
                new2.next = head2
                new2 = new2.next
            head2 = head2.next
        
        if head2.val != repeat:
            new2.next = head2
        else:
            new2.next = None
            
        return new.next

          
