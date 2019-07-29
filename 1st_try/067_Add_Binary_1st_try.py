'''
99.75%
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = a[::-1],b[::-1]
        
        len_a = len(a)
        len_b = len(b)
        
        if len_a > len_b:
            b = b + str(0) * (len_a-len_b)
        else:
            a = a + str(0) * (len_b-len_a)
            
        carry = 0
        output = ''
        
        for i in range(len(a)):
            if a[i] == b[i]:
                current = carry
                if a[i] == '0':    
                    carry = 0
                elif a[i] == '1':
                    carry = 1
                    
            elif a[i] != b[i]:
                if carry == 1:
                    current, carry = 0, 1
                elif carry == 0:
                    current,carry = 1, 0

            output = output + str(current)
            
        if carry == 1:
            output = output + str(1)
            
        return output[::-1]
                
        
