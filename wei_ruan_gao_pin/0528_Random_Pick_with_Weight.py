class Solution:

    def __init__(self, w: List[int]):
        summation = 0
        self.sum_list = []
        for item in w:
            summation += item
            self.sum_list.append(summation)
        self.summation = summation        

    def pickIndex(self) -> int:
        target = self.summation * random.random()
        start,end = 0, len(self.sum_list)
        while start<=end:
            mid = (start+end)//2
            if target<self.sum_list[mid]:
                end = mid-1
            else:
                start = mid+1
        return start

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
