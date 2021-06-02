class Solution:
    def calculate(self, s: str) -> int:
        
        number = 0
        symbol = '+'
        stack = []
        for i in range(len(s)):
            if s[i]==' ':
                continue
            if s[i].isdigit():
                number = number*10+int(s[i])
                if i+1==len(s) or (not s[i+1].isdigit()):
                    if symbol =='*':
                        stack[-1]*=number
                    elif symbol=='/':
                        stack[-1] = int(stack[-1]/ number)
                    elif symbol=='+':
                        stack.append(number)
                    elif symbol=='-':
                        stack.append(-number)
            else:
                symbol = s[i]
                number=0

        return sum(stack)
