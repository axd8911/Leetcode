# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #val and node into a tuple and put into list, create heap
        #pop the smallest and push its next node, if it has next
        curr = output = ListNode(0)
        cmp = [(lists[idx].val,idx) for idx in range(len(lists)) if lists[idx]]
        heapq.heapify(cmp)

        while cmp:
            value, index = heapq.heappop(cmp)
            curr.next = lists[index]
            lists[index] = lists[index].next
            curr = curr.next
            if lists[index]:
                heapq.heappush(cmp,(lists[index].val,index))

        return output.next
