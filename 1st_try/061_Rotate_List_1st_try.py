'''
99.47%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:        
        if head == None:
            return head
        head2 = head
        cnt = 0
        while head2 != None:
            head2 = head2.next
            cnt = cnt + 1
        if k%cnt == 0:
            return head
        
        move = cnt - k % cnt
        head2 = head
        
        for i in range(move-1):
            print (head2.val)
            head2 = head2.next
            
        temp = head2.next
        head2.next = None
        
        temp2 = temp
        while temp2.next != None:
            temp2= temp2.next
        
        temp2.next = head
        
        return temp
        
 
