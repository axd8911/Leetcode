'''
99.83%
Braining burning problem. Hard to control linked list positions. Should give more try!
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        num = n - m
        
        cnt = 1
        head2 = head
        while cnt < m:
            
            #if m == 1:
            #    starter = head2
            if cnt == m-1:
                starter = head2
            head2 = head2.next
            cnt = cnt + 1
                     
        backup = target = head2
        rest = target.next
        target.next = None
        
        for i in range(num):
            other = rest.next
            rest.next = target
            target = rest
            rest = other
        
        backup.next = other
        if m == 1:
            return target
        else:
            starter.next = target
        
                  
        return head
            
        
            
        
