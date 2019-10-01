class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #iterate all items from beginning
        if not nums:
            return 1

        idx = 0
        while idx<len(nums):
            loc = nums[idx]-1
            if nums[idx]>len(nums) or nums[idx]<=0:
                nums[idx] = 0
                idx+=1

            elif nums[idx] != idx + 1:
                if nums[loc] == nums[idx]:
                    nums[idx] =0
                    idx+=1
                else:
                    nums[idx],nums[loc] = nums[loc],nums[idx]
            else:
                idx+=1

        for i in range(len(nums)):
            if i != nums[i]-1:
                return i+1
        return len(nums)+1
