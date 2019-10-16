class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums = nums * 2
        res = [-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            while stack:
                if stack[-1]<=nums[i]:
                    stack.pop()
                else:
                    res[i] = stack[-1]
                    break
            stack.append(nums[i])

        #print (res)
        return res[:len(res)//2]
                
