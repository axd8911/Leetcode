class Solution:
    def numberToWords(self, num: int) -> str:
        print (num)
        if num == 0:
            return 'Zero'
        output = ''
        if num >= 10**9:
            digit = num//10**9
            num = num % 10**9
            output += self.threeDigits(digit) + ' Billion'
        if num >= 10**6:
            digit = num//10**6
            num = num % 10**6
            output += self.threeDigits(digit) + ' Million'
        if num >= 10**3:
            digit = num//10**3
            num = num % 10**3
            output += self.threeDigits(digit) + ' Thousand'
        output +=  self.threeDigits(num)
        if output[0] == ' ': return output[1:]
        return output

    def threeDigits(self,num):
        words = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
        tens = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
        output = ''
        if num >= 100:
            digit = num//100
            num = num % 100
            output += ' ' + words[digit] + ' Hundred'
        if num>=20:
            digit = num//10
            num = num % 10
            output += ' ' + tens[digit]
        if num>0:
            output += ' ' + words[num]
        return output
