'''
81.58% for both

'''


#iteration
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        output = [[]]
        
        for item1 in nums:
            new = []
            for set1 in output:
                new.append(set1+[item1])
            output = output + new
            
        output2 = []
        
        for item in output:
            if item not in output2:
                output2.append(item)
            
        
        return output2
        

#recursion
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        output = [[]]
        
        def bt(allSet,combine):
            if combine not in output:
                output.append(combine)
            
            for i in range(len(allSet)):
                bt(allSet[i+1:], combine + [allSet[i]])
                
                
        if nums:
            bt(nums,[])
        '''    
        output2 = []
        for item in output:
            if item not in output2:
                output2.append(item)
        '''        
        return output
        
