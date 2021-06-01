class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = [(-count[item],item) for item in count]
        heapq.heapify(heap)
        output = heapq.nsmallest(k,heap)
        return [item[1] for item in output]
