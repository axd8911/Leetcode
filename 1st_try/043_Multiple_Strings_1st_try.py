'''
48.77%. Fastest runs all should be direct multiply, which is not allowed in the problem.
This is a problem requesting multiple digit by digit. It is easy in Python.

'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        result = 0
        carry1 = 1
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for item1 in num1:
            carry2 = 1
            for item2 in num2:
                result += int(item1) * int(item2) * carry1 * carry2
                carry2 *= 10
            carry1 *= 10    
                
        return str(result)
                
        
