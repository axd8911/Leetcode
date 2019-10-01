class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        match = {')':'(',']':'[','}':'{'}
        stack = []

        for item in s:
            if item not in match:
                stack.append(item)
            else:
                if not stack or stack[-1] != match[item]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False
