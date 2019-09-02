class Solution:
    def costOfTree(self,leaves):
        stack = [2**32-1]
        output = 0
        length = len(leaves)
        for leaf in leaves:
            while stack[-1] <= leaf:
                curr = stack.pop()
                output += curr * min(leaf,stack[-1])
            stack.append(leaf)
        while len(stack)>2:
            output += stack.pop() * stack[-1]
        return output


    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            if min_index == 0:
                ans += arr[0] * arr[1]
                arr = arr[1:]
            elif min_index == len(arr) - 1:
                ans += arr[-1] * arr[-2]
                arr = arr[:-1]
            else:
                ans += arr[min_index] * min(arr[min_index + 1], arr[min_index - 1])
                arr = arr[:min_index] + arr[min_index + 1:]
        return ans
