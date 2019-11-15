class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        total = 0
        while len(sticks)>1:
            n1 = heapq.heappop(sticks)
            n2 = heapq.heappop(sticks)
            curr = n1 + n2
            total += curr
            heapq.heappush(sticks,curr)

        return total
            
