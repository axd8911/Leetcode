'''
98%
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head:
            """
            Do not return anything, modify head in-place instead.
            """
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            part2 = slow.next
            slow.next = None

            end = []
            while part2:
                end.append(part2)
                part2 = part2.next
            end = end[::-1]

            output = head
            n = 0

            while output and n < len(end):
                save = output.next
                output.next = end[n]
                end[n].next = save
                output = output.next.next
                n = n + 1


        
            
            
            
            
