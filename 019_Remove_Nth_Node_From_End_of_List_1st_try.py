'''
90.45%

Solution1: two linked list passes is just normal approach.
Solution2: One linked list pass is very interesting. Keep a gap and then go to the end.

'''


# Solution1
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        total = 0
        head2 = head
        while head2:
            head2 = head2.next
            total = total + 1
        head2 = head   
        order = 0
        while head:
            if total-n == 0:
                return head.next
            if order == total-n-1:
                head.next = head.next.next
            order = order + 1
            head = head.next

        return head2
                
#Solution2
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        explorer = stander = head
        gap = 0
        while gap < n:
            gap = gap + 1
            explorer = explorer.next
        
        if explorer == None:
            return head.next
        
        while explorer.next:            
            explorer = explorer.next
            stander = stander.next
            
        stander.next = stander.next.next
        
        return head
                
