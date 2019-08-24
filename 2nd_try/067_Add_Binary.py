class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = a[::-1],b[::-1]
        la,lb = len(a),len(b)

        if lb>la:
            a += '0'*(lb-la)
        if la>lb:
            b+='0'*(la-lb)
        length = len(a)

        carry = '0'
        result = ''
        n=0
        #print (a,b)
        while n<length:
            total = 0
            total += int(carry) + int(a[n]) + int(b[n])
            if total%2 == 0:
                result += '0'
            else:
                result += '1'
            if total//2 == 0:
                carry = '0'
            else:
                carry = '1'

            n+=1

        if carry == '1':
            result+='1'
        return result[::-1]
