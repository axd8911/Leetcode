'''
99.26%

Full copy and partial copy?
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        repeat = 0
        accu = 1
        n = 1
        while n < len(nums):
            if nums[n] == nums[n-1]:
                repeat = repeat + 1   
                
                if repeat <= 1:
                    nums[accu] = nums[n]
                    accu = accu + 1
                    
            if nums[n] != nums[n-1]:
                nums[accu] = nums[n]
                accu = accu + 1
                repeat = 0

            n = n + 1
        
        nums[:] = nums[:accu]
        
        

                
        
                
        
