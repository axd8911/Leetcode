'''
72.5%
a very good practice for linked list address allocation. Should try a few more times, make the thought clearer and do some similar problems.

'''



class Solution(object):
    def swapPairs(self, head):
                
        bb = bb2 = ListNode(0)
        bb2.next = head
        while head and head.next:
            a1 = head
            b1 = head.next
            c1 = head.next.next
            
            b = b1
            b.next = a1
            a1.next = c1
            
            bb2.next = b
            bb2 = bb2.next.next
            head = head.next
        return bb.next
      

        
