'''
73%.

I feel a bit clearer about linked list, though sometimes it is still 玄学. 
You should control the node assignment in linked list, but not let them control you.

It requires constant memory, which means you should not assign new list. Meaning that only a fixed memory for temp linked list nodes is allowed.

'''



class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        nodes = []
        head3 = head2 = ListNode(0)
        head2.next = head
        while head:  
            nodes.append(head)
            n = n + 1
            if n == k:  
                head2.next = head
                temp = head.next
                for i in range(len(nodes)-1,-1,-1):
                    head.next = nodes[i] 
                    head = head.next
                    head2 = head2.next
                head.next = temp
                nodes = []
                n = 0

            head = head.next
        return head3.next
