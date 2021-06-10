class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = '0'
        output = ''
        idx = 0
        while idx<len(a) or idx<len(b):
            part_a = '0' if idx>=len(a) else a[idx]
            part_b = '0' if idx>=len(b) else b[idx]
            curr = int(part_a) + int(part_b) + int(carry)
            if curr ==3:
                output += '1'
                carry = '1'
                
            elif curr==2:
                output += '0'
                carry = '1'
            
            elif curr ==1:
                output += '1'
                carry = '0'
            
            else:
                output += '0'
                carry = '0'
            idx +=1
        if carry == '1':
            output += carry
        
        return output[::-1]
