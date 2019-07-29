'''
99.79%
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = 0
        cnt = 0
        while n < len(nums):
            if nums[n] == 0:
                nums.insert(0,nums.pop(n))
                n = n + 1
                cnt = cnt + 1
            elif nums[n] == 1:
                n = n + 1
                cnt = cnt + 1
            elif nums[n] == 2:
                nums.append(nums.pop(n))
                cnt = cnt + 1
            if cnt == len(nums):
                break
                

#a good solution in Leetcode
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = j = 0
        
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            # @this index, get it original value, change it to 2
            if v <= 1:
                nums[i] = 1
                i = i + 1
            # if value <= 1
            if v == 0:
                nums[j] = 0
                j = j + 1
            
        
