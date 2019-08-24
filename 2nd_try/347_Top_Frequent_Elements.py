class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        cntList = [(cnt[key]*(-1),key) for key in cnt]
        heapq.heapify(cntList)
        output = []
        for i in range(k):
            output.append(heapq.heappop(cntList)[1])
        return output
