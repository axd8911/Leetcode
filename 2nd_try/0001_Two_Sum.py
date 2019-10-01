class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}

        for i in range(len(nums)):
            if target-nums[i] in past:
                return [past[target-nums[i]],i]
            else:
                past[nums[i]] = i
