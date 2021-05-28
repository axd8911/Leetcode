# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        output = curr = ListNode(0)
        heaplists = []
        ip = 0
        lists = [item for item in lists if item]
        
        for item in lists:
            heapq.heappush(heaplists,(item.val,ip,item))
            ip+=1
            
        while heaplists:
            popout = heapq.heappop(heaplists)
            curr.next = popout[2]
            curr = curr.next
            if popout[2].next:
                heapq.heappush(heaplists,(popout[2].next.val,ip,popout[2].next))
            ip+=1
        return output.next
    #time O(MNlogK)
    #space O(MN)
