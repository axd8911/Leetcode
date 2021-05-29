class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = -float('inf')
        summation = 0
        for num in nums:
            summation += num
            output = max(summation, output)
            if summation <0:
                summation = 0
        return output
