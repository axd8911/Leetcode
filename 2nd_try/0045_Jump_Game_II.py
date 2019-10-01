class Solution:
    def jump(self, nums: List[int]) -> int:
        step, far, cur = 0,0,0
        for i in range(len(nums)-1):
            if i+nums[i]>far:
                far = i+nums[i]
            if i==cur:
                step+=1
                cur = far
        return step
