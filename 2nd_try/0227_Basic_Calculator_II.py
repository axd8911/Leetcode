class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'
        op = '+'
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-1*num)
                elif op == '*':
                    stack[-1]*=num
                elif op == '/':
                    stack[-1] = int(stack[-1]/num)
                num, op = 0, c
        return sum(stack)
