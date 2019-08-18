class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        for i in range(len(nums)-k+1):
            result = heapq.heappop(nums)
        return result
