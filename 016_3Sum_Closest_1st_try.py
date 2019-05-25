'''
90.83%

Learned from YouTube video
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[-1]
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            
            j = i + 1
            k = len(nums)-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(temp - target) < abs(closest-target):
                    closest = temp
                
                if temp == target:
                    return temp
                elif temp > target:
                    k = k - 1
                else:
                    j = j + 1
            

        return closest
