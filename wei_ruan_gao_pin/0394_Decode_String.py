class Solution:
    def decodeString(self, s: str) -> str:
        currNum = 0
        currStr = ''
        stack = []
        for c in s:
            if c=='[':
                stack.append(currStr)
                stack.append(currNum)
                currStr=''
                currNum=0
            elif c==']':
                prevNum=stack.pop()
                prevStr=stack.pop()
                currStr = prevStr+prevNum*currStr
            elif c.isdigit():
                currNum=currNum*10+int(c)
            else:
                currStr+=c
        return currStr
