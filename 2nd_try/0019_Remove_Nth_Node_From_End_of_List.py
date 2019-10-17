class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = ListNode(0)
        fast.next = head
        i = 0
        while fast and fast.next:
            fast = fast.next

            if i>=n:
                slow = slow.next
            i +=1

        if i==n:
            return head.next

        slow.next = slow.next.next
        return head
