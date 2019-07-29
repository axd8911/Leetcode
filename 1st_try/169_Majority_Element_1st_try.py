'''
100%
'''



#solution 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        
        return nums[len(nums)//2]


#solution 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        for item in nums:
            if item not in count:
                count[item] = 1
            else:
                count[item] = count[item] + 1
            if count[item]>len(nums)/2:
                return item
