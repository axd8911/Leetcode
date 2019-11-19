class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        twice = nums + nums
        stack = []
        res = []
        for i in range(len(twice)-1,-1,-1):
            while stack:
                if twice[i]>=stack[-1]:
                    stack.pop()
                else:
                    break
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(twice[i])
        return res[::-1][:len(nums)]
