# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        res = curr = ListNode(0)
        myheap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(myheap,(lists[i].val,i,lists[i]))

        while myheap:
            value,idx,node = heapq.heappop(myheap)
            curr.next = node
            node = node.next
            if node:
                heapq.heappush(myheap,(node.val,idx,node))
            curr = curr.next

        return res.next
        
