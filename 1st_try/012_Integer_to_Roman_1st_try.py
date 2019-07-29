'''
60%

classify ones and fives in each digit and then match them one by one
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        
        one = ['M','C','X','I']
        five = ['','D','L','V']
        

        
        d1 = num%10
        d2 = num%100 - d1
        d3 = num%1000 - d1 -d2
        d4 = num - d1 - d2 - d3
        
        number = [int(d4/1000),int(d3/100),int(d2/10),int(d1)]
        
        r = ['','','','']
        
        for i in range(4):
            if number[i] <= 3:
                r[i] = number[i] * one[i]
            if number[i] == 4:
                r[i] = one[i] + five[i]
                
            if number[i] >= 5 and number[i] <= 8:
                r[i] = five[i] + (number[i] - 5) * one[i]
            if number[i] == 9:
                r[i] = one[i] + one[i-1]
                
                
        return ''.join(r) 
        

        
