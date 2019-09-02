import collections
import heapq
class Solution:
    def meetingRoom(self, intervals):
        # iterate all intervals
        room = collections.defaultdict(int)
        for i,j in intervals:
            for point in range(i,j):
                room[point] += 1
        biggest = 0
        for key in room:
            biggest = max(room[key],biggest)
        return biggest

    def meetingRoom2(self,intervals):
        room = [intervals[0][1]]
        heapq.heapify(room)
        intervals.sort()
        print (intervals)
        for i,j in intervals[1:]:
            print (room)
            earliest = heapq.heappop(room)
            if earliest <= i:   # no conflict
                heapq.heappush(room,j)
            else:
                heapq.heappush(room,earliest)
                heapq.heappush(room,j)
        return len(room)

def main():
    intervals = [[0, 30],[5, 10],[15, 20],[9,16],[7,12]]
    result = Solution().meetingRoom2(intervals)
    print (result)

main()
