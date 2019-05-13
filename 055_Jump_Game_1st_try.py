'''
99.17%

Could use enumerate to achieve shorter code and same results.
The value should be bigger than the distance in order to jump over 0 values.
'''



class Solution:
    def canJump(self, nums: List[int]) -> bool:

        for i in range(len(nums)-1):
            if nums[i] == 0:
                checker = nums[i::-1]
                for j in range(len(checker)):
                    go = False
                    if checker[j] > j:
                        go = True
                        break
                if go == False:
                    return go
                
        return True
        
