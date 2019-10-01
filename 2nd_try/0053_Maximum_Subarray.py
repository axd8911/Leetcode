class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if sum of some front items is bigger than 1, it can still make some contribution. If not, back zero. Negative numbers will not be useful.

        curr = 0
        maximum = float('-inf')

        for item in nums:

            curr += item
            maximum = max(maximum,curr)
            if curr < 0:
                curr = 0


        return maximum
