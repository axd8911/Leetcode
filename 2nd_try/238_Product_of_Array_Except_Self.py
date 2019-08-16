class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)
        l, r = 1, 1
        for i in range(1,len(nums)):
            l*=nums[i-1]
            output[i] = l

        for j in range(len(nums)-2,-1,-1):
            r*=nums[j+1]
            output[j] *= r
            
        return output
