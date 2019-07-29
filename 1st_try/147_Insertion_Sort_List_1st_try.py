# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        res1 = res2 = head
             
        while head.next:
            if head.next.val < head.val:
                
                temp = head.next
                head.next = head.next.next
                
                if temp.val < res2.val:
                    temp.next = res2
                    res2 = res1 = temp
                else:
                    while res2:

                        if temp.val < res2.next.val:
                            temp2 = res2.next
                            res2.next = temp
                            temp.next = temp2
                            break
                        
                        res2 = res2.next
                    res2 = res1
            
            else:
                head = head.next
            
        return res1
            
