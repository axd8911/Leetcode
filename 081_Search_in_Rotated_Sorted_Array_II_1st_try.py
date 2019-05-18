'''
97.35%
Make sure all steps are optimized. e.g., remove repeat values from the list

'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        if nums == []:
            return False
        
        nums2 = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums2.append(nums[i])
                        
        nums = nums2
        
        loc = len(nums2)
        accu = 0
        while True:
            loc = len(nums2) // 2
            if nums2[loc] > nums2[-1]:
                accu = accu + loc
                nums2 = nums2[loc:]
            elif nums2[loc] < nums2[-1]:
                nums2 = nums2[:loc+1]
            else:
                if nums2[loc-1] > nums2[loc]: accu = accu + loc
                break
                
        nums2 = nums[accu:] + nums[:accu]
        loc = len(nums2)
        while nums2:
            loc = len(nums2) // 2
            if nums2[loc] > target:
                nums2 = nums2[:loc]
            elif nums2[loc] < target:
                nums2 = nums2[loc+1:]
            else:
                return True
            
        return False
            
        
