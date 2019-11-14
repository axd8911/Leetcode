class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x:x[0]**2+x[1]**2)
        return points[:K]


#------------------------------------------------------------#
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        myHeap = []
        cnt = 0
        for x,y in points:
            cnt += 1
            heapq.heappush(myHeap,(-(x**2+y**2),(x,y)))
            if cnt>K:
                heapq.heappop(myHeap)

        return [item[1] for item in myHeap]
