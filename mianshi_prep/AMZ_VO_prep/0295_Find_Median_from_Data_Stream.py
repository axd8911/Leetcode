class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:        
        if len(self.l) > len(self.r):
            heapq.heappush(self.r,-heapq.heappushpop(self.l,-num))
        else:
            heapq.heappush(self.l,-heapq.heappushpop(self.r,num))

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return -self.l[0]
        else:
            return (self.r[0]-self.l[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
