class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordFreq = collections.Counter(words)
        freqList = [(wordFreq[key]*(-1),key) for key in wordFreq]
        heapq.heapify(freqList)
        return [heapq.heappop(freqList)[1] for _ in range(k)]
