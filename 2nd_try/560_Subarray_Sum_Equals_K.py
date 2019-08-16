class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #we want k. we add up till now and obtain sum. if any 0 - j total is (sum-k), they meet our need

        total = 0
        appear = collections.defaultdict(int)
        appear[0]=1                         # we need to add nothing so that sum is 0
        cnt = 0

        for item in nums:
            total += item                   # sum till now
            cnt += appear[total-k]          # how many sum-k appeared before
            appear[total] += 1              # put current sum for future use
            # current sum can only be used for the future, not now. Otherwise total-k tells us 0-curr is total,while a zero length int is k. such int does not exist
        return cnt
