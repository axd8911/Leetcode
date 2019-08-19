class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ''
        curNum = 0

        for c in s:
            if c == '[':                            # if there is a [
                stack.append(curString)             # save current string and number and prepare for the new []
                stack.append(curNum)
                curString = ''
                curNum = 0

            elif c == ']':                          # if there is a ]
                num = stack.pop()                   # the amount of string in new [], with the previous string in front, if any
                prevString = stack.pop()
                curString = prevString + curString*num


            elif c.isdigit():
                curNum = 10*curNum+int(c)

            else:
                curString += c

        return curString
