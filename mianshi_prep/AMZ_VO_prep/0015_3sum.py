class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            target = -nums[i]
            while l<r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1

                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res
                
