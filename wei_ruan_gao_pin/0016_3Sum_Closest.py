class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minimum = inf
        res = nums[0]+nums[1]+nums[-1]
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total==target:
                    return target
                if abs(total-target)<minimum:
                    minimum = abs(total-target)
                    res = total
                if total>target:
                    r-=1
                else:
                    l+=1
        return res
