class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for a,b in points:
            distance = a*a+b*b
            heapq.heappush(res,(distance,[a,b]))
        output = []
        for i in range(k):
            output.append(heapq.heappop(res)[1])
        return output
