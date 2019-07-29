'''
~50%

Did not jump out in time.

Good to learn backtracking
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def backtracking(nums,temp,remainder,index):
            if remainder == 0:
                output.append(temp[:])
            if remainder <= 0:
                return
            for i in range(index, len(nums)):
                temp.append(nums[i])
                backtracking(nums,temp,remainder - nums[i], i)
                temp.pop()

                
        if candidates:
            backtracking(candidates,[],target,0)
            
        return output
