'''
Leetcode score: 54%
A normal approach: add numbers in each position
if one number used out, we can add the rest of the other number to the new number, or make up zeros and still add one by one

Make good use of the following code:
sumation2 = sumation1 = ListNode(0): in what cases will one variable change by following another?

'''







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        goNext = 0
        summation2 = summation1 = ListNode(0)
        # I have to write some comments here: sum1 and sum2 seems to be sharing the same memory: later when I assign sth to sum2, sum1 will also get that value

        while l1 or l2:

            temp_sum = l1.val + l2.val + goNext
            goNext = int(temp_sum/10)
            summation2.next = ListNode(temp_sum % 10)
            summation2 = summation2.next            

            if l1.next == None and l2.next == None:
                break
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)

            l1 = l1.next
            l2 = l2.next
 
        if goNext == 1:
            summation2.next = ListNode(1)

        return summation1.next
