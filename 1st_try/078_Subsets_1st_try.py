'''
99.87%
backtracking
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        allSet = nums
        
        def dp(allSet, combine,index):
            output.append(combine)
            for i in range(len(allSet)):
                dp(allSet[i+1:],combine+[allSet[i]],i+1)
                
        if nums:
            dp(allSet,[],0)
            
        return output
            
