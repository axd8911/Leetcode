class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        start = max(nums)
        end = sum(nums)

        def helper(nums,target,groups):
            total = 0

            for i in range(len(nums)):
                #print (target,total)
                total+=nums[i]
                if total > target:
                    total = nums[i]
                    groups -= 1
                if groups == 0:
                    return -1
            return 0

        while start <= end:
            mid = (start + end)//2
            judge = helper(nums,mid,m)
            if judge == 0:
                end = mid - 1
            else:
                start = mid+1

        return start
