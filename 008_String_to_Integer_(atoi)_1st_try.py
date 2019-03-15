'''
Based on comments in Leetcode.com, this is a 'shity' problem - testing you how to use if else.
Useless.

~50%
'''

class Solution:
    def myAtoi(self, str: str) -> int:
        
        number = []
        for item in str:

            if len(number)==0 and item == ' ':
                continue
            if (item not in ['1','2','3','4','5','6','7','8','9','0','-','+']):
                break
                
            if len(number)!=0 and item ==' ':
                break

            number.append(item)
                
        if number == []:
            return 0
        
        if len(number) > 1 and '+' in number[1:]:
            number = number[0:number[1:].index('+')+1]
               
        if len(number) > 1 and '-' in number[1:]:
            number = number[0:number[1:].index('-')+1]
   
        if len(number) == 1 and number[0] in ['+','-']:
            return 0        
                    
        number = int(''.join(number))
        
        if number > 2**31-1:
            return 2147483647
        if number < -2**31:
            return -2147483648        
        return number
