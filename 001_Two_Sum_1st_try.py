'''
Leetcode score: 76%
Be aware that you refered to a solution.
The main idea is using search of a dictionary. Should come back and repeat
run time level (n)

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        for index_1, num_1 in enumerate(nums):
            #print (lookup)
            if target - num_1 in lookup:
                return [index_1, lookup[target-num_1]]
                break
            lookup.update({num_1:index_1})
        
        
