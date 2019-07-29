'''
90%
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        curr = []
        
        for item in tokens:

            if item == '+':
                curr.append(int(curr.pop()) + int(curr.pop()))
            elif item == '-':
                curr.append(- int(curr.pop()) + int(curr.pop()))
            elif item == '*':
                curr.append(int(curr.pop()) * int(curr.pop()))
            elif item == '/':
                curr.append(int(1/int(curr.pop()) * int(curr.pop())))
            else:
                curr.append(item)
                
        return int(curr[0])
                
