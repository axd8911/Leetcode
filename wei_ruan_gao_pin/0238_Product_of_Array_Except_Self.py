class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        frontToEnd = [1]
        endToFront = [1]
        res = []
        
        for i in range(len(nums)-1):
            frontToEnd.append(frontToEnd[-1]*nums[i])
        for i in range(len(nums)-1,0,-1):
            endToFront.append(endToFront[-1]*nums[i])
        endToFront = endToFront[::-1]
        for i in range(len(nums)):
            res.append(frontToEnd[i]*endToFront[i])
        return res
            
