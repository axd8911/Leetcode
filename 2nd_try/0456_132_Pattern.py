class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        stack = []
        mini = []
        mini.append(nums[0])
        for i in range(len(nums)):
            mini.append(min(mini[-1], nums[i]))

        for i in range(len(nums)-1,-1,-1):
            if nums[i] > mini[i]:
                while stack and stack[-1]<=mini[i]:
                    stack.pop()
                if stack and stack[-1]<nums[i]:
                    return True
                stack.append(nums[i])
        return False
