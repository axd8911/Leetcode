class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        myHeap = []
        for x,y in intervals:
            if not myHeap:
                heapq.heappush(myHeap,y)
            else:
                if x>=myHeap[0]:
                    heapq.heappushpop(myHeap,y)
                else:
                    heapq.heappush(myHeap,y)
        return len(myHeap)
