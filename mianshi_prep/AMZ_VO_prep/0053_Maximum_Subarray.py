class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxi = float('-inf')
        for item in nums:
            total+=item
            maxi = max(maxi,total)
            if total<0:
                total=0

        return maxi
