class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        length = []
        
        for i in range(len(s)):
            if stack and s[i]==stack[-1]:
                length[-1]+=1
                if length[-1]==k:
                    stack.pop()
                    length.pop()
            else:
                stack.append(s[i])
                length.append(1)
        output = ''
        for i in range(len(stack)):
            output += stack[i]*length[i]
        return output
        
