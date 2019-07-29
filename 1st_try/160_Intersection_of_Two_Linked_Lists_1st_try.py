# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        dumA = headA
        dumB = headB
        
        while dumA != dumB:
            if dumA != None:
                dumA = dumA.next
            else:
                dumA = headB
            if dumB != None:
                dumB = dumB.next
            else:
                dumB = headA
                
        return dumA
