'''
93.5%

one for loop is enough. Add up items - if items sum is smaller than 0, clear the sum to 0 because the previous set has negative impact.
Whenever a temp_sum is bigger than current maximum, replace it, even if temp_sum is smaller than 0.
'''




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum = nums[0]
        temp_sum = 0
        for item in nums:
            temp_sum = temp_sum + item
            if temp_sum > maximum:
                maximum = temp_sum
            if temp_sum < 0:
                temp_sum = 0
                
        return maximum
