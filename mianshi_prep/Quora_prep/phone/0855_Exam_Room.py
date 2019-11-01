class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.occu = [(self._dis(-1,N),-1,N)]

    def seat(self) -> int:
        gap,x,y = heapq.heappop(self.occu)

        if x == -1:
            res = 0
        elif y == self.N:
            res = self.N - 1
        else:
            res = (x+y)//2
        heapq.heappush(self.occu,(self._dis(x,res),x,res))
        heapq.heappush(self.occu,(self._dis(res,y),res,y))
        return res


    def leave(self, p: int) -> None:
        for item in self.occu:
            if item[1] == p:
                gap1,startp,end = item
            if item[2] == p:
                gap2,start,endp = item
        self.occu.remove((gap1,startp,end))
        self.occu.remove((gap2,start,endp))
        heapq.heapify(self.occu)
        heapq.heappush(self.occu,(self._dis(start,end),start,end))


    def _dis(self,start,end):
        if start == -1:
            return -end
        elif end == self.N:
            return -(self.N-1-start)
        else:
            return -((end-start)//2)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
