class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def bt(left,right,combine):
            #print (combine)
            if len(combine) == 2*n:
                output.append(combine)

            if left < n:
                bt(left+1,right,combine+'(')

            if right < left:
                bt(left,right+1,combine+')')

        bt(0,0,'')
        return output
