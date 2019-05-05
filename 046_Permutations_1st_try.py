'''
75%

Use some force to loop through all possibilities. The search code could be improved by recording indices.
Tried dynamic programming for a long time. Still not so familiar with it...
'''

class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return [[]]
        
        currentCmb = [[item] for item in nums]
        
        for i in range(len(nums)-1):
            newCmb = []
            for item1 in currentCmb:
                tempSet = [item2 for item2 in nums if item2 not in item1]
                for number in tempSet:
                    newCmb.append(item1+[number])
                    
            currentCmb = newCmb
        return currentCmb
