# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # a sub function to do the reverse. Define the reverse length. If not enough node, it should revert back
        
        def reverseOneGroup(node, k):
            count = 0
            copy = node
            while copy:
                count += 1
                copy = copy.next
                if copy == None and count<k:
                    return node,None
                if count == k:
                    break
            
            curr = node
            while count > 1 and curr and curr.next:
                to_front = curr.next
                save = curr.next.next
                to_front.next = node
                curr.next = save
                node = to_front
                count -=1
            return node,curr
        
        curr = backup = ListNode(0)
        curr.next = head
        while curr:
            head,tail=reverseOneGroup(head,k)
            curr.next = head
            curr = tail
            if curr:
                head = tail.next

        return backup.next
            
