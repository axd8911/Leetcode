class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        total = 0
        appear = collections.defaultdict(int)
        appear[0] = 1
        for num in nums:
            total += num
            cnt += appear[total-k]
            appear[total] += 1
        return cnt
