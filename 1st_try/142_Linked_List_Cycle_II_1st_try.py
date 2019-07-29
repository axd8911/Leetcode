'''
97%

First, count the number of items in cycle
Second, locate the start position of the cycle
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        double = single = head
        start = False
        repeat = 0
        n = 0
        while True:
            
            if double == None or double.next == None or double.next.next == None:
                return None
            
            double = double.next.next
            single = single.next
         
            if repeat == 2:
                
                cycle = n
                break            
            
            if double == single:
                start = True
                repeat = repeat + 1
            if repeat == 1:
                n = n + 1

        slow = fast = head
        n = 0
        while n < cycle:
            fast = fast.next
            n = n + 1
        count = 0
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
            count = count + 1

        print (count)
        return fast
            
            
