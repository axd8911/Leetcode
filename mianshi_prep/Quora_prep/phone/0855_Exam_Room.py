class ExamRoom:
    def __init__(self, N: int):

        self.N = N
        self.occupy = []

    def seat(self) -> int:
        if not self.occupy:
            res = 0
        else:
            d = self.occupy[0]
            res = 0
            for i in range(1,len(self.occupy)):
                if d < (self.occupy[i] - self.occupy[i-1])//2:
                    d = (self.occupy[i] - self.occupy[i-1])//2
                    res = (self.occupy[i] + self.occupy[i-1])//2
            if d<self.N-1-self.occupy[-1]:
                res = self.N - 1
        bisect.insort(self.occupy,res)
        return res

    def leave(self, p: int) -> None:
        self.occupy.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
