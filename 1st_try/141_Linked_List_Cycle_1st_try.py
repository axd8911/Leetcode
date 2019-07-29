'''
same as CC189 2_8. Dictionary solves the problem.
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        head_dict = {}
        n = 0
        
        while head:
            if head not in head_dict:
                head_dict[head] = n
                head = head.next
                n = n + 1
            else:
                return True
        
        return False
        
        
        """
        :type head: ListNode
        :rtype: bool
        """
        
