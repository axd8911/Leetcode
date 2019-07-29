'''
86%

Useful to understand linked list

'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        
        result1 = result2 = ListNode(0)

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                result2.next = l1
                l1 = l1.next         
            else:
                result2.next = l2
                l2 = l2.next
            
            result2 = result2.next
        
        if l1 != None:
            result2.next = l1
            
        if l2 != None:
            result2.next = l2

        return result1.next
            
        
