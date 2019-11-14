# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = curr = ListNode(0)

        myHeap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(myHeap,(lists[i].val,i,lists[i]))

        while myHeap:
            val, index, node = heapq.heappop(myHeap)
            curr.next = node
            node = node.next
            curr = curr.next

            if node:
                heapq.heappush(myHeap,(node.val,index,node))

        return res.next
            
