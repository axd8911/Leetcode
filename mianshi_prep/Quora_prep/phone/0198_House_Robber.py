class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        has = nums[0]
        hasNo = 0

        for i in range(1,len(nums)):
            has,hasNo = hasNo+nums[i],max(has,hasNo)

        return max(has,hasNo)
