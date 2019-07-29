'''
Two approaches: convert to string and do reverse, or use %10 and add up

1st: 83.8%
2nd: 62%

attention that -3%10 == 7, need some treatment. No other difficulties

'''

#in string
class Solution:
    def reverse(self, x: int) -> int:
       
        x = str(x)
        if x[0] == '-':
            x = x[0] + x[:0:-1]
        else: x = x[::-1]
            
        x = int(x)
        if x <= -2**31 or x>= 2**31 -1:
            return 0
            
        return x
        
#in numeric:
class Solution:
    def reverse(self, x: int) -> int:

        y = 0
        
        if x < 0: x_calc = 0 - x
        else: x_calc = x
        
        while x_calc != 0:

                y = x_calc%10 + y * 10
                x_calc = int(x_calc/10)                
                
        if y <= -2**31 or y>= 2**31 -1:
            return 0
        
        if x < 0: return -y
        else: return y
