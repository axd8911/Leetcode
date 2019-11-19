class Solution(object):
    def topKFrequent(self, words, k):
        timeCount = collections.Counter(words)
        myHeap = []
        for key in timeCount:
            heapq.heappush(myHeap,[-timeCount[key],key])
        res = []
        cnt = k
        while cnt>0:
            res.append(heapq.heappop(myHeap)[1])
            cnt-=1
        return res
