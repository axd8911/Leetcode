'''
Iteration:64%
Recursion: Much slower

'''

#Iteration
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        rest = []
        for i in range(len(nums)):
            rest.append([a for a in range(i)]+[a for a in range(i+1,len(nums))])
        temp = [(item,) for item in nums]
        current = dict(zip(temp,rest))

        for i in range(len(nums)-1):
            new = {}
            for key in current:
                for j in range(len(current[key])):
                    new[key+(nums[current[key][j]],)] = current[key][:j] + current[key][j+1:]     
            current = new
            
        return [list(item) for item in current.keys()]
            
        
 #Recursion
 class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        length = len(nums)
        
        def goAll(combine, nums):
            if len(combine) == length and combine not in output:
                output.append(combine[:])
                return
            
            for i in range(len(nums)):
                combine.append(nums[i])
                goAll(combine,nums[:i]+nums[i+1:])
                combine.pop()
                
        if nums:
            goAll([],nums)
            
        return output
        
        
        
