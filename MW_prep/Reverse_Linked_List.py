class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self,head):
        curr = head
        while curr.next:
            new = curr.next
            save = curr.next.next
            new.next = head
            head = new
            curr.next = save
        return head


                    
