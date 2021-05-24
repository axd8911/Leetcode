class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        matchOne = {0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five', 6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten', 11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
        matchTwo = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
                
        def twoDigit(num):
            if 0<= num<20:
                return matchOne[num]
            else:
                return (matchTwo[num//10] + ' ' + matchOne[num%10]).strip()
            
        def threeDigit(num):
            if 0<=num<100:
                return twoDigit(num)
            else:
                return (matchOne[num//100] + ' Hundred ' + twoDigit(num%100)).strip()
        
        output = ''
        if num//10**9>0:
            output += threeDigit(num//10**9) + ' Billion '
            num -= (num//10**9*10**9)
        if num//10**6>0:
            output += threeDigit(num//10**6) + ' Million '
            num -= (num//10**6*10**6)
        if num//10**3>0:
            output += threeDigit(num//10**3) + ' Thousand '
            num -= (num//10**3*10**3)

        if num > 0:
            output += threeDigit(num)

        return output.strip()
            
