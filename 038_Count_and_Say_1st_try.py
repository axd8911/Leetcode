'''
84.9%

Pay attention to the boundary conditions
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        
        currentNum = '1'
        
        for i in range(1,n):
            newNum = ''
            count = 1
            for j in range(1,len(currentNum)):
                if currentNum[j-1] == currentNum[j]:
                    count = count + 1       
                else:
                    newNum = newNum + str(count) + currentNum[j-1]
                    count = 1
            newNum = newNum + str(count) + currentNum[-1]
            currentNum = newNum

        return (currentNum)
                
        
