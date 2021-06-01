class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack: save index
        # loop to curr: it can save all items in stack that has lower temperature and update its waiting output
        output = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                last = stack.pop()
                output[last] = i-last
            stack.append(i)
        return output
